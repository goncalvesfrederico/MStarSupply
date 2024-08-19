import { BASE_URL } from '../App';
import React, { useEffect, useState } from 'react'
import { Flex, Spinner, Text, TableContainer, Table, TableCaption, Thead, Tr, Th, Tbody, Td, Tfoot } from '@chakra-ui/react'

const FollowUpTable = ({followUp, setFollowUp}) => {
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const getFollowUp = async () => {
            try {
                const res = await fetch(BASE_URL + "/followup");
                const data = await res.json();

                if (!res.ok) {
                    throw new Error(data.error);
                }
                setFollowUp(data);
            } catch (error) {
                console.error(error);
            } finally {
                setIsLoading(false);
            }
        }
        getFollowUp();
    }, [setFollowUp])

    console.log(followUp);

    return (
        <>
            <TableContainer>
                <Table variant='striped' colorScheme='teal'>
                    <TableCaption>Follow Up - Movimentações de Marcadorias</TableCaption>
                    <Thead>
                        <Tr>
                            <Th>ID</Th>
                            <Th>Tipo Movimentação</Th>
                            <Th>Mercadoria</Th>
                            <Th>Usuário</Th>
                            <Th>Local</Th>
                            <Th isNumeric>Quantidade</Th>
                            <Th>Data Movimento</Th>
                        </Tr>
                    </Thead>
                    <Tbody>
                        {followUp.map((movimentacao) => (
                            <Tr key={movimentacao.id}>
                                <Td>{movimentacao.id}</Td>
                                <Td>{movimentacao.tipoMovimentacaoId}</Td>
                                <Td>{movimentacao.mercadoriaId}</Td>
                                <Td>{movimentacao.userId}</Td>
                                <Td>{movimentacao.localId}</Td>
                                <Td isNumeric>{movimentacao.quantidade}</Td>
                                <Td>{new Date(movimentacao.dataMovimento).toLocaleString()}</Td>
                            </Tr>
                        ))}
                    </Tbody>
                    <Tfoot>
                        <Tr>
                            <Th>ID</Th>
                            <Th>Tipo Movimentação</Th>
                            <Th>Mercadoria</Th>
                            <Th>Usuário</Th>
                            <Th>Local</Th>
                            <Th isNumeric>Quantidade</Th>
                            <Th>Data Movimento</Th>
                        </Tr>
                    </Tfoot>
                </Table>
            </TableContainer>

            {/* se nao tiver movimentacoes na database */}
            {isLoading && (
                <Flex justifyContent={"center"}>
                    <Spinner size={"x1"} />
                </Flex>
            )}
            {/* nao possue movimentacoes */}
            {!isLoading && followUp.lenght === 0 && (
                <Flex justifyContent={"center"}>
                    <Text fontSize={"x1"}>
                        <Text as={"span"} fontSize={"2x1"} fontWeight={"bold"} mr={2}>
                            Não existe Movimentações de entrada e saída.
                        </Text>
                    </Text>
                </Flex>
            )}
        </>
    )
}

export default FollowUpTable