#  File: Poly.py

#  Description: Program to find the sum and product of two polynomials using linked list

#  Student Name: Jiaxin Huang

#  Date Created: 04/15/2021

#  Date Last Modified: 04/15/2021

import sys

class Link (object):
    def __init__ (self, coeff = 1, exp = 1, next = None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__ (self):
        return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
    def __init__ (self):
        self.first = None

    # helper function to find length of list
    def get_num_links(self):
        length = 0 # set count variable
        current = self.first
        if (current == None): # return 0 if empty
            return 0
        # increment length and move to next link until end of link
        while (current != None):
            length += 1
            current = current.next
        return length

    # keep Links in descending order of exponents
    def insert_in_order (self, coeff, exp):
        new_link = Link(coeff, exp) # create new link
        previous = self.first   # keep track of link before to compare
        current = self.first
        # if list is empty set the new link as first
        if (self.first == None):
            self.first = new_link
            return
        # continue looping if the new exponent is less than the current exponent
        while (exp <= current.exp):
            # set the last link as new link if current was last
            if (current.next == None):
                current.next = new_link
                return
            else:
                # move on
                previous = current
                current = current.next
        # break out loop when exp > current.exp
        # make new link the first link if current was first 
        if (current == self.first):
            new_link.next = self.first
            self.first = new_link
        else:
            # place the new link between the previous and current link
            previous.next = new_link
            new_link.next = current
        
    # add polynomial p to this polynomial and return the sum
    def add (self, p):
        # create new list to store sums
        result_sum = LinkedList()
        my_term = self.first
        other_term = p.first
        # return list p if self is empty
        if (self.get_num_links() == 0):
            return p
        # return list self if p is empty
        elif (p.get_num_links() == 0):
            return self
        else:
            # continue looping until both terms reach end
            while ((my_term != None) and (other_term != None)):
                # add the coeff of two terms and keep exp if the exp are the same
                if (my_term.exp == other_term.exp):
                    result_coeff = my_term.coeff + other_term.coeff
                    result_sum.insert_in_order(result_coeff, my_term.exp)
                    # move on for both since taken account of
                    my_term = my_term.next
                    other_term = other_term.next
                # add other_term if its exp is bigger
                elif (my_term.exp < other_term.exp):
                    result_sum.insert_in_order(other_term.coeff, other_term.exp)
                    # move on only for other_term since my_term was not used or added
                    other_term = other_term.next
                # add my_term if its exp is bigger
                elif (my_term.exp > other_term.exp):
                    result_sum.insert_in_order(my_term.coeff, my_term.exp)
                    # move on only for my_term since other_term was not used or added
                    my_term = my_term.next
        # loop to make sure all the terms in my_term is added to list or combined with other_term
        while (my_term != None):
            result_sum.insert_in_order(my_term.coeff, my_term.exp)
            my_term = my_term.next
        # loop to make sure all the terms in other_term is added to list or combined with my_term
        while (other_term != None):
            result_sum.insert_in_order(other_term.coeff, other_term.exp)
            other_term = other_term.next
        return result_sum
        

    # multiply polynomial p to this polynomial and return the product
    def mult (self, p):
        # create new list to store sums
        result_product = LinkedList()
        my_term = self.first
        other_term = p.first
        # return list p if self is empty
        if (self.get_num_links() == 0):
            return p
        # return list self if p is empty
        elif (p.get_num_links() == 0):
            return self
        else:
            # multiply each term of the first polynomial with every term in the second polynomial
            for i in range(self.get_num_links()):
                other_term = p.first    # reset the second polynomial 
                for j in range(p.get_num_links()):
                    # multiply the coefficient of both to find result coeff
                    result_coeff = my_term.coeff * other_term.coeff
                    # add the exponents of both to find the resulting exponent 
                    result_exp = my_term.exp + other_term.exp
                    # insert the term result in order
                    result_product.insert_in_order(result_coeff, result_exp)
                    other_term = other_term.next    # move on to next term in second polynomial
                my_term = my_term.next  # move on to next term in first polynomial
        return result_product

    # helper function to simplify the polynomial so exp is not repeated
    def simplify(self):
        # return itself if the list is empty
        if (self.get_num_links() == 0):
            return self
        # if there is more than 1 links in list
        elif (self.get_num_links() > 1):
            first_cur = self.first
            # two loops to compare next link to see if exp match
            while (first_cur != None):
                sec_cur = first_cur.next
                while (sec_cur != None):
                    # if the first link exp matches the second link exp
                    if (first_cur.exp == sec_cur.exp):
                        # add them together and set final as first link
                        first_cur.coeff = first_cur.coeff + sec_cur.coeff
                        first_cur.next = sec_cur.next   # skip the second link since added to first
                        sec_cur = sec_cur.next  # move on to see if next one match
                    else:   # if it does not match, break out of the loop
                        break
                first_cur = first_cur.next  # move to next link

    # helper function to clean zero coefficients
    def clean(self):
        # create a new list
        clean_ver = LinkedList()
        current = self.first
        # loop through list and add it to new list if it does not have 0 coeff
        for i in range(self.get_num_links()):
            # skip the link if the coeff is 0
            if (current.coeff == 0):
                current = current.next
            else:
                clean_ver.insert_in_order(current.coeff, current.exp)
                current = current.next
        return clean_ver


    # create a string representation of the polynomial
    def __str__ (self):
        strng = "" # create empty string
        current = self.first
        # return empty string if list is empty
        if (self.first == None):
            return ""
        else:
            # add all the terms of the polynomial to strng
            for i in range(self.get_num_links()):
                # if the current is last link, no addition symbol
                if (current.next == None):
                    strng += str(current)
                else:
                    strng += str(current) + " + "
                    current = current.next
        return strng


def main():
    # read data from file poly.in from stdin
    line_p = (sys.stdin.readline()).strip()
    num_terms_p = int(line_p)
  
    # create polynomial p
    p = LinkedList()
    for i in range(num_terms_p):
        term = (sys.stdin.readline()).strip().split(" ")
        coeff = int(term[0])
        exp = int(term[1])
        p.insert_in_order(coeff, exp)
    # print(p)
    # create polynomial q
    space = sys.stdin.readline()
    line_q = (sys.stdin.readline()).strip()
    num_terms_q = int(line_q)
    q = LinkedList()
    for i in range(num_terms_q):
        term = (sys.stdin.readline()).strip().split(" ")
        coeff = int(term[0])
        exp = int(term[1])
        q.insert_in_order(coeff, exp)
    # print(q)

    # get sum of p and q and print sum
    result_sum = p.add(q)
    result_sum.simplify()
    clean_ver = result_sum.clean()
    # print(result_sum)
    print(clean_ver)

    # get product of p and q and print product
    result_product = p.mult(q)
    # simplified_product = result_product.simplify()
    result_product.simplify()
    clean_ver_prod = result_product.clean()
    # print(result_product)
    print(clean_ver_prod)

if __name__ == "__main__":
    main()