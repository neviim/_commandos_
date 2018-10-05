# O MongoDB suporta uma variedade de operadores condicionais, incluindo:

$eq     (igual a)
$lt 	(menor que)
$lte 	(menor ou igual a)
$gt 	(maior que)
$gte 	(maior ou igual a)
$all 	(corresponder a todos os valores em um array)
$exists (verificar se um campo existe ou não)
$mod 	(módulo)
$ne 	(não igual)
$in 	(corresponder a um ou mais valores em um array)
$nin 	(corresponder a valores zero em um array)
$nor 	(não corresponder uma consulta nem outra)
$size 	(corresponder qualquer array com número definido de elementos)
$type 	(corresponder valores com tipo de dados BSON especificado)

# Operadores logicos

$not 	(não igual a)
$nor    (consulta com um NOR lógico retorna todos os documentos que não correspondem a ambas cláusulas.)
$or 	(corresponder uma consulta a outra)
$and    (logical AND retorna todos os documentos que correspondem às condições de ambas cláusulas.)