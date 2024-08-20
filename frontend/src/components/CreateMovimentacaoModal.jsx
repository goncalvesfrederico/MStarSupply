import { BASE_URL } from '../App'
import React, { useEffect, useState } from 'react'
import { BiAddToQueue } from "react-icons/bi"
import { Button, Modal, ModalOverlay, useDisclosure, ModalHeader, ModalContent, ModalCloseButton, ModalBody, Flex, FormControl, FormLabel, Input, ModalFooter, useToast, RadioGroup, Radio, Select } from '@chakra-ui/react'

const CreateMovimentacaoModal = ({ setFollowUp }) => {
    const { isOpen, onOpen, onClose } = useDisclosure();
    const [isLoading, setIsLoading] = useState(false);
    const [inputs, setInputs] = useState({
            tipoMovimentacaoId: "",
            mercadoriaId: "",
            userId: "",
            localId: "",
            quantidade: "",
    });
    const toast = useToast()
    
    const [mercadorias, setMercadorias] = useState([])
    useEffect(() => {
        const fecthMercadorias = async () => {
            try {
                const res = await fetch(BASE_URL + "/mercadorias")
                const data = await res.json();
                if (!res.ok) {
                    throw new Error(data.error)
                }
                setMercadorias(data);
            } catch (error) {
                console.error(error);
            }
        };
        fecthMercadorias();
    }, []);

    const [usuarios, setUsuarios] = useState([]);
    useEffect(() => {
        const fetchUsuarios = async () => {
            try {
                const res = await fetch(BASE_URL + "/users")
                const data = await res.json()
                if (!res.ok) {
                    throw new Error(data.error)
                }
                setUsuarios(data);
            } catch (error) {
                console.error(error);
            }
        };
        fetchUsuarios();
    }, []);

    const [locais, setLocais] = useState([])
    useEffect(() => {
        const fetchLocais = async () => {
            try {
                const res = await fetch(BASE_URL + "/locais")
                const data = await res.json()
                if (!res.ok) {
                    throw new Error(data.error)
                }
                setLocais(data);
            } catch (error) {
                console.error(error);
            }
        };
        fetchLocais();
    }, []);

    const handleCreateMovimentacao = async (e) => {
        e.preventDefault() // prevent page to refresh/reload
        setIsLoading(true)

        try {
            const res = await fetch(BASE_URL + "/followup", {
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
                description: "Movimentação gravada com sucesso! Confira o Follow Up.",
                status: 'success',
                duration: 3000,
                position: "top-center"
            });
            onClose();
            setFollowUp((prevFollowUp) => [...prevFollowUp, data]) // adding new movimentacao

            // clear inputs
            setInputs({
                tipoMovimentacaoId: "",
                mercadoriaId: "",
                userId: "",
                localId: "",
                quantidade: "",
            })

        } catch (error) {
            toast({
                title: 'Ocorreu um erro na gravação',
                description: error.message,
                status: 'error',
                duration: 4000,
                position: "top-center"
            })
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <>
            <Button onClick={onOpen} >
                <BiAddToQueue size={20} />
            </Button>

            <Modal isOpen={isOpen} onClose={onClose}>
                <ModalOverlay>
                    <form onSubmit={handleCreateMovimentacao}>
                        <ModalContent>
                            <ModalHeader>Nova Movimentação  💾</ModalHeader>
                            <ModalCloseButton />
                            <ModalBody pb={6}>
                                <RadioGroup mt={4}>
                                    <Flex gap={5}>
                                        <Radio value="1"
                                            onChange={(e) => setInputs({...inputs, tipoMovimentacaoId: parseInt(e.target.value)})}
                                        >Entrada</Radio>
                                        <Radio value="2"
                                            onChange={(e) => setInputs({...inputs, tipoMovimentacaoId: parseInt(e.target.value)})}
                                        >Saída</Radio>
                                    </Flex>
                                </RadioGroup>

                                <Select 
                                    mt={4} 
                                    placeholder="Selecione a mercadoria"
                                    value={inputs.mercadoriaId}
                                    onChange={(e) => setInputs({...inputs, mercadoriaId: e.target.value})}
                                >
                                    {mercadorias.map((produto) => (
                                        <option key={produto.id} value={produto.id}>{produto.nome}</option>
                                    ))}
                                </Select>

                                <Select 
                                    mt={4} 
                                    placeholder="Selecione o usuario"
                                    value={inputs.userId}
                                    onChange={(e) => setInputs({...inputs, userId: e.target.value})}
                                >
                                    {usuarios.map((user) => (
                                        <option key={user.id} value={user.id}>{user.nome}</option>
                                    ))}
                                </Select>

                                <Select 
                                    mt={4} 
                                    placeholder="Selecione o local/almoxarifado"
                                    value={inputs.localId}
                                    onChange={(e) => setInputs({...inputs, localId: e.target.value})}
                                >
                                    {locais.map((local) => (
                                        <option key={local.id} value={local.id}>{local.nome}</option>
                                    ))}
                                </Select>

                                <FormControl mt={4}>
                                    <FormLabel>Quantidade</FormLabel>
                                    <Input
                                        type='number'
                                        placeholder='Quantidade'
                                        value={inputs.quantidade}
                                        onChange={(e) => setInputs({...inputs, quantidade: parseInt(e.target.value) || ""})}
                                    />
                                </FormControl>

                            </ModalBody>
                            <ModalFooter>
                                <Button colorScheme='blue' mr={3} type='Submit' isLoading={isLoading}>Salvar</Button>
                                <Button onClick={onClose}>Cancel</Button>
                            </ModalFooter>
                        </ModalContent>
                    </form>
                </ModalOverlay>
            </Modal>
        </>
    )
};

export default CreateMovimentacaoModal