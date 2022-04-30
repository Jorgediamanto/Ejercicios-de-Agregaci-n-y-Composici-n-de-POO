#el mensaje yang ha sio destruido se muestra al final porque aunque destruyamos yang, yang sigue estando referenciado en yin, por lo que al destruir yin habra que destruir yang.
#por lo que para que el mensaje salga antes, tienes que destruir tambien yin, como he hecho abajo

class Yin: pass 
class Yang: 
    def __del__(self): 
        print("Yang destruido") 
 
yin = Yin() 
yang = Yang() 
yin.yang = yang 

print(yin)
print(yang is yin.yang)

del(yin)
del(yang)
print("?")
print("?")
print("?")

