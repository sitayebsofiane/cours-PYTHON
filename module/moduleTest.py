#coding:utf-8
"""
module pour le joueeur
"""
def parler(perssonage,message):
    print("{} : {}".format(perssonage,message))
def aurevoir():
    print("Aurevoir")
# on test le moduleTest
if __name__ == "__main__":
    print("phase de test de moduleTest")
    parler("jason","bonjour tout le monde")
    aurevoir()