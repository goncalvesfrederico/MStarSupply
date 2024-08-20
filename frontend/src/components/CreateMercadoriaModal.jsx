import { BASE_URL } from '../App'
import React, { useEffect, useState } from 'react'
import { SiShutterstock } from "react-icons/si";
import { Button, Modal, ModalOverlay, useDisclosure, ModalHeader, ModalContent, ModalCloseButton, ModalBody, Flex, FormControl, FormLabel, Input, ModalFooter, useToast, RadioGroup, Radio, Select, Textarea } from '@chakra-ui/react'

const CreateMercadoriaModal = ({ setMercadorias }) => {
    const { isOpen, onOpen, onClose } = useDisclosure();
    const [isLoading, setIsLoading] = useState(false);
    const [inputs, setInputs] = useState({
        nome: "",
        numeroRegistro: "",
        descricao: "",
        estoque: "",
        fabricanteId: "",
        categoriaId: "",
    });
    const toast = useToast()

    const [fabricantes, setFabricantes] = useState([])
    useEffect(() => {
        const fetchFabricantes = async () => {
            try {
                const res = await fetch(BASE_URL + "/fabricantes")
                const data = await res.json();
                if (!res.ok) {
                    throw new Error(data.error)
                }
                setFabricantes(data);
            } catch (error) {
                console.error(error);
            }
        };
        fetchFabricantes();
    }, []);
    
    const [categorias, setCategorias] = useState([])
    useEffect(() => {
        const fetchCategorias = async () => {
            try {
                const res = await fetch(BASE_URL + "/categorias")
                const data = await res.json();
                if (!res.ok) {
                    throw new Error(data.error)
                }
                setCategorias(data);
            } catch (error) {
                console.error(error);
            }
        };
        fetchCategorias();
    }, []);

    const handleCreateMercadoria = async (e) => {
        e.preventDefault()
        setIsLoading(true)

        try {
            const res = await fetch(BASE_URL + "/mercadorias", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(inputs),
            })
            const data = await res.json();
            if (!res.ok) {
                throw new Error(data.error)
            }

            toast({
                title: 'Movimentação gravada.',
                description: "Movimentação gravada com sucesso! Confira as mercadorias.",
                status: 'success',
                duration: 3000,
                position: "top-center"
            });
            onClose();
            setMercadorias((prevMercadorias) => [...prevMercadorias, data]) //adding new mercadoria

            // clear inputs
            setInputs({
                nome: "",
                numeroRegistro: "",
                descricao: "",
                estoque: "",
                fabricanteId: "",
                categoriaId: "",
            })
        } catch (error) {
            toast({
                title: 'Ocorreu um erro na gravação',
                description: error.message,
                status: 'error',
                duration: 9000,
                position: "top-center"
            })
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <>
            <Button onClick={onOpen}>
                <SiShutterstock size={20} />
            </Button>

            <Modal isOpen={isOpen} onClose={onClose}>
                <ModalOverlay/>
                <form onSubmit={handleCreateMercadoria}>
                    <ModalContent>
                        <ModalHeader>Nova Mercadoria  💾</ModalHeader>
                        <ModalCloseButton />
                        <ModalBody pb={6}>
                            <Flex alignItems={"center"} gap={4}>
                                {/* Left */}
                                <FormControl>
                                    <FormLabel>Nome</FormLabel>
                                    <Input placeholder='iPad Pro 13" 1Gb' 
                                        value={inputs.nome} 
                                        onChange={(e) => setInputs({...inputs, nome: e.target.value})} 
                                    />
                                </FormControl>

                                {/* Right */}
                                <FormControl>
                                    <FormLabel>Numero do Registro</FormLabel>
                                    <Input placeholder='ABC123' 
                                        value={inputs.numeroRegistro}
                                        onChange={(e) => setInputs({...inputs, numeroRegistro: e.target.value})}
                                    />
                                </FormControl>
                            </Flex>

                            <FormControl mt={4}>
                                <FormLabel>Descrição</FormLabel>
                                <Textarea resize={"none"} 
                                    overflowY={"hidden"} 
                                    placeholder="Produto possui x configurações" 
                                    value={inputs.descricao} 
                                    onChange={(e) => setInputs({...inputs, descricao: e.target.value})}
                                />
                            </FormControl>

                            <FormControl mt={4}>
                                <FormLabel>Estoque</FormLabel>
                                <Input placeholder='99999'
                                    value={inputs.estoque}
                                    onChange={(e) => setInputs({...inputs, estoque: parseInt(e.target.value)})}
                                />
                            </FormControl>

                            <FormControl mt={4}>
                                <FormLabel>Fabricante</FormLabel>
                                <Select mt={2}
                                    placeholder='Selecione o fabricante'
                                    value={inputs.fabricanteId}
                                    onChange={(e) => setInputs({...inputs, fabricanteId: e.target.value})}
                                >
                                    {fabricantes.map((fabricante) => (
                                        <option key={fabricante.id} value={fabricante.id}>{fabricante.nome}</option>
                                    ))}
                                </Select>
                            </FormControl>

                            <FormControl mt={4}>
                                <FormLabel>Categoria</FormLabel>
                                <Select mt={2}
                                    placeholder='Selecione a categoria'
                                    value={inputs.categoriaId}
                                    onChange={(e) => setInputs({...inputs, categoriaId: e.target.value})}
                                >
                                    {categorias.map((categoria) => (
                                        <option key={categoria.id} value={categoria.id}>{categoria.nome}</option>
                                    ))}
                                </Select>
                            </FormControl>
                        </ModalBody>
                        <ModalFooter>
                            <Button colorScheme='blue' mr={3} type='Submit' isLoading={isLoading}>Salvar</Button>
                            <Button onClick={onClose}>Cancel</Button>
                        </ModalFooter>
                    </ModalContent>
                </form>
            </Modal>
        </>
    )
};

export default CreateMercadoriaModal