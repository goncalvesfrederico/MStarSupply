import React from 'react'
import { BiTrash } from 'react-icons/bi'
import { Card, CardHeader, Flex, Box, Heading, Text, IconButton, CardBody, useToast } from '@chakra-ui/react'
import { BASE_URL } from '../App'

const MercadoriaCard = ({mercadoria, setMercadorias}) => {
    const toast = useToast();
    
    // function to delete the mercadorias
    const handleDeleteMercadoria = async () => {
        try {
            const res = await fetch(BASE_URL + "/mercadorias/" + mercadoria.id, {
                method: "DELETE"
            })
            const data = await res.json();
            if (!res.ok) {
                throw new Error(data.error)
            }
            setMercadorias((prevMercadorias) => prevMercadorias.filter((m) => m.id !== mercadoria.id))
            toast({
                title: "Sucesso",
                description: "Mercadoria foi excluída com sucesso!",
                status: "success",
                duration: 2000,
                inClosable: true,
                position: "top-center"
            })
        } catch (error) {
            toast({
                title: "Ocorreu um erro",
                description: error.message,
                status: "error",
                duration: 4000,
                inClosable: true,
                position: "top-center"
            })
        }
    }

    return (
        <Card>
            <CardHeader>
                <Flex gap={"4"}>
                    <Flex flex={"1"} gap={"4"} alignItems={"center"}>
                        <Box>
                            <Heading size="sm">{mercadoria.id}</Heading>
                            <Heading size="sm">{mercadoria.nome}</Heading>
                            <Text>Numero de Registro: {mercadoria.numeroRegistro}</Text>
                            <Text>Estoque: {mercadoria.estoque}</Text>
                            <Text>Fabricante: {mercadoria.fabricanteId}</Text>
                            <Text>Categoria: {mercadoria.categoriaId}</Text>
                        </Box>
                    </Flex>

                    {/* delete icon */}
                    <Flex>
                        {/* TODO: fazer a parte da edicao da mercadoria */}
                        {/* <EditMercadoria user={mercadoria} setMercadorias={setMercadorias} /> */}
                        <IconButton 
                            variant="ghost" 
                            colorScheme='red' 
                            size={"sm"} 
                            aria-label='See menu' 
                            icon={<BiTrash size={20} 
                            onClick={handleDeleteMercadoria}
                        />} />
                    </Flex>
                </Flex>
            </CardHeader>

            <CardBody>
                <Heading size="sm">Descrição</Heading>
                <Text>{mercadoria.descricao}</Text>
            </CardBody>
        </Card>
    )
}

export default MercadoriaCard