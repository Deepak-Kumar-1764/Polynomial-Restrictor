from tkinter import*


#*Print Polynomial*#

# define a fun that combine coeff,var and return polynomial
def print_polynomial(coefficients):
    final_result = []
    for term, coeff in coefficients.items():  #pick coeff and var from dict 1 by 1

        if term.startswith('x'):      #x1*x2^3
            final_result.append(str(f"{coeff}*{term}"))
            final_result.append(str("+"))
        else:                                 #constant
            final_result.append(str(f"{coeff}"))
            final_result.append(str("+"))
    final_result= final_result[:-1]
    return final_result




#constructing a dictionary that contains key->variable and value->coefficient
def parse_polynomial(polynomial,k):
    terms = polynomial.split('+')  # Split the polynomial into terms

    coefficients = {}
    for term in terms:
        term = term.strip()  # Remove any leading or trailing whitespace
        if term:
            if '*' in term:  # If the term contains a '*', it's a product term
                parts = term.split('*')
                coeff = 1
                variables = []
                for part in parts:
                    if part.startswith('x'):  # Check if the part is a variable
                        variables.append(part)
                    else:
                        coeff *= int(part)            # Otherwise, it's a constant
                                       # Combine variables into a key, store coefficient with that key
                variables_key = '*'.join(variables)
                coefficients[variables_key] = coeff%k
                if coefficients[variables_key]==0:
                    del coefficients[variables_key]
            elif term.startswith('x'):  # If the term starts with 'x', it's a single variable
                coefficients[term] = 1
            else:                        # Otherwise, it's a constant
                coefficients[term] = int(term)%k
                if coefficients[term]==0:
                    del coefficients[term]

    return coefficients



#*Partial assighnment*#
def parse_variable_input(input_string):
    variables_values = {}   #creat an empty dict
    pairs = input_string.split(',')    #x1=1,x2=3 split with comma
    for pair in pairs:
        variable, value = pair.split('=') 
        variable = variable.strip()     # Remove leading/trailing whitespace
        value = int(value.strip())  # Convert value to integer and remove whitespace
        variables_values[variable] = value
    return variables_values

def search_key(dictionary, key):  #for checking previously exist var
    return key in dictionary

def partially_polynomial(polynomial,variables_values,k):
    terms = polynomial.split('+')  # Split the polynomial into terms
    temp=0
    temp2=''
    coefficients = {}
    for term in terms:
        term = term.strip()  # Remove any leading or trailing whitespace
        if term:
           
            if '*' in term:  # If the term contains a '*', it's a product term
               
                parts = term.split('*')
                coeff = 1
                variables = []
                for part in parts:
                    if '^' in part:
                        tmp=part.split('^')
                        s=int(tmp[1])
                        if part.startswith('x') and search_key(variables_values,tmp[0]):  # Check if the part is a variable
                        
                            coeff*=variables_values[tmp[0]]**s
                        elif part.startswith('x') and not search_key(variables_values,tmp[0]) :
                         # Check if the part is a variable
                            variables.append(part)
                    else:
                        if part.startswith('x') and search_key(variables_values,part):  # Check if the part is a variable
                        
                            coeff*=variables_values[part]
                        
                        elif part.startswith('x') and not search_key(variables_values,part) :  # Check if the part is a variable
                            variables.append(part)
                        else:
                            
                            coeff *= int(part)  # Otherwise, it's a constant
                # Combine variables into a key, store coefficient with that key
               
                variables_key = '*'.join(variables)
                if len(variables_key)==0:
                    temp+=coeff
               
                if(search_key(coefficients,variables_key)):
                    coefficients[variables_key] += coeff
                    coefficients[variables_key] = coefficients[variables_key]%k
                    if coefficients[variables_key]==0:
                        del coefficients[variables_key]
                else:
                    coefficients[variables_key] = coeff%k
                    if coefficients[variables_key]==0:
                        del coefficients[variables_key]
            elif term.startswith('x') and '^' in term:#and not search_key(variables_values,term):  # If the term starts with 'x', it's a single variable
                
                tmp=term.split('^')
                s=int(tmp[1])
                if search_key(variables_values,tmp[0]):
                    temp+=variables_values[tmp[0]]**s
                elif search_key(coefficients,term):
                    coefficients[term] += 1
                else:
                    coefficients[term] = 1
            elif term.startswith('x') and search_key(variables_values,term):  # If the term starts with 'x', it's a single variable
                
                temp+=  variables_values[term]
            elif term.startswith('x') and  not search_key(variables_values,term):
                    if search_key(coefficients,term):
                        coefficients[term] += 1
                    else:
                        coefficients[term] = 1
            else:  # Otherwise, it's a constant
                temp+=int(term)
                
    coefficients[temp2]=temp%k

       
    return coefficients


