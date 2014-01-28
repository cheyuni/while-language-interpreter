# -----------------------------------------------------------------------------
# interpreter.py
#
# 2013 10 25 lex, yacc while language interpreter
# cheyuni_
# -----------------------------------------------------------------------------
import pprint

class EnvMem: #manage environment and memory
    def __init__(self, parent):
        self.env = dict()
        self.mem = dict()
        if(parent == None):
            self.parent = None
        else:
            self.parent = parent
    
    def set_mem_env(self, env_name, mem_data, flag):
        if flag == 'DECLARE':
            index = len(self.mem.keys())
            self.env[env_name] = index
            self.mem[index] = mem_data
        elif flag == 'ASSIGN':
            if(self.env.has_key(env_name)):
                index = self.env[env_name]
                self.mem[index] = mem_data
            else:
                if self.parent:
                    self.parent.set_mem_env(env_name, mem_data, 'ASSIGN')
                
    def get_name_value(self, name):
        if self.env.has_key(name):
            return self.mem[self.env[name]]
        else:
            return self.parent.get_name_value(name)

    def print_all(self):
        print '\nenv :',
        print self.env
        print 'mem :',
        print self.mem
        if self.parent:
            self.parent.print_all()
        else :
            print "\n"
    
    def print_value_all(self):
        for key, value in self.env.items():
            print key,
            print self.mem[value]
        if self.parent:
            self.parent.print_value_all()
        else :
            print "\n"
    
import sys
class Interpreter:
    def __init__(self):
        init = sys.argv[1]
        # init = 5
        self.codes = [('DECLARE', 'ret'), ('PROC', 'fib', (('NAME', 'n'), ('DECLARE', 'tmp'), ('ASSIGN', 'ret', ('INT', '1')), ('ASSIGN', 'tmp', ('UMINUS', ('INT', '1'))), ('WHILE', ('AND', ('BANG', ('EQUAL', ('NAME', 'n'), ('INT', '1'))), ('BANG', ('EQUAL', ('NAME', 'n'), ('INT', '2')))), (('DECLARE', 'local'), ('ASSIGN', 'local', ('MINUS', ('NAME', 'ret'), ('NAME', 'tmp'))), ('ASSIGN', 'tmp', ('UMINUS', ('NAME', 'ret'))), ('ASSIGN', 'ret', ('NAME', 'local')), ('ASSIGN', 'n', ('MINUS', ('NAME', 'n'), ('INT', '1'))))))), ('PROC', 'sum', (('NAME', 'n'), ('IF', ('LT', ('NAME', 'n'), ('INT', '1')), ('SKIP',), (('FUNCTION_CALL', 'sum', ('MINUS', ('NAME', 'n'), ('INT', '1'))), ('ASSIGN', 'ret', ('PLUS', ('NAME', 'ret'), ('NAME', 'n'))))))), ('IF', ('LT', ('NAME', 'in'), ('INT', '1')), ('SKIP',), (('FUNCTION_CALL', 'sum', ('NAME', 'in')), ('FUNCTION_CALL', 'fib', ('NAME', 'ret')), ('PRINT', ('NAME', 'ret'))))] #code structure from lexer, yacc
        self.init_em = EnvMem(None) #initialize env
        self.init_em.set_mem_env('in', init, 'DECLARE')
        self.current_em = self.init_em
        for code in self.codes:
            self.code_evaluator(code)
            
    def __del__(self):
        print "\nprogram ended\n"
        
    def code_evaluator(self, code):
        if(code[0] == 'DECLARE'):
            self.current_em.set_mem_env(code[1], 0, code[0])
        elif(code[0] == 'ASSIGN'):
            self.current_em.set_mem_env(code[1], self.code_evaluator(code[2]), code[0])
        elif(code[0] == 'PROC'):
            proc = code[2] 
            self.current_em.set_mem_env(code[1], proc, 'DECLARE')
        elif(code[0] == 'IF'):
            new_em = EnvMem(self.current_em)
            self.current_em = new_em
            if self.code_evaluator(code[1]):
                if len(code[2]) == 1:
                    self.code_evaluator(code[2])
                else:
                    for token in code[2]:
                        self.code_evaluator(token)
            else:
                if len(code[3]) == 1:
                    self.code_evaluator(code[3])
                else:
                    for token in code[3]:
                        self.code_evaluator(token)
            self.current_em = self.current_em.parent
        elif(code[0] == 'WHILE'):
            while self.code_evaluator(code[1]):
                new_em = EnvMem(self.current_em)
                self.current_em = new_em
                for token in code[2]:
                    self.code_evaluator(token)
                self.current_em = self.current_em.parent
        elif(code[0] == 'NAME'):
            return self.current_em.get_name_value(code[1])
        elif(code[0] == 'BANG'):
            return not self.code_evaluator(code[1])
        elif(code[0] == 'UMINUS'):
            return -self.code_evaluator(code[1])
        elif(code[0] == 'PLUS'):
            return self.code_evaluator(code[1]) + self.code_evaluator(code[2])
        elif(code[0] == 'MINUS'):
            return self.code_evaluator(code[1]) - self.code_evaluator(code[2])
        elif(code[0] == 'MUL'):
            return self.code_evaluator(code[1]) * self.code_evaluator(code[2])            
        elif(code[0] == 'DIVIDE'):
            return self.code_evaluator(code[1]) / self.code_evaluator(code[2])            
        elif(code[0] == 'LT'):
            if self.code_evaluator(code[1]) < self.code_evaluator(code[2]):
                return True
            else:
                return False
        elif(code[0] == 'FUNCTION_CALL'):
            new_em = EnvMem(self.current_em)
            self.current_em = new_em
            param = ('INT', self.code_evaluator(code[2]))
            proc_codes = self.current_em.get_name_value(code[1])
            self.code_evaluator(('DECLARE', proc_codes[0][1]))
            self.code_evaluator(('ASSIGN', proc_codes[0][1], param))
            for code in proc_codes[1:]:
                self.code_evaluator(code)
            self.current_em = self.current_em.parent
        elif(code == 'SKIP'):
            pass
        elif(code[0] == 'INT'):
            return int(code[1])
        elif(code[0] == 'EQUAL'):
            return self.code_evaluator(code[1]) == self.code_evaluator(code[2])
        elif(code[0] == 'AND'):
            return self.code_evaluator(code[1]) and self.code_evaluator(code[2])
        elif(code[0] == 'PRINT'):
            print "while language print : " + str(self.code_evaluator(code[1]))

inter = Interpreter()
