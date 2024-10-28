import clases

persona = clases.persona()


persona.setNombre("Mauricio")
persona.setAltura("170cm")
persona.setApellidos("Ospina Tabares")
persona.setEdad(42)


print(f"la persona es {persona.getNombre()} {persona.getApellidos()} tiene {persona.getEdad()}")


informatico = clases.Informatico()


informatico.setNombre("Laura")
informatico.setAltura("155cm")
informatico.setApellidos("Muñoz Serrano")
informatico.setEdad(30)

print(f"la persona es {informatico.getNombre()} {informatico.getApellidos()} tiene {informatico.getEdad()}")


