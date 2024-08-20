import { IoMoon } from "react-icons/io5";
import { LuSun } from "react-icons/lu";
import CreateMovimentacaoModal from "./CreateMovimentacaoModal";
import { Container, useColorMode, Box, useColorModeValue, Flex, Text, Button } from "@chakra-ui/react"

const Navbar = ({setFollowUp}) => {
    const { colorMode, toggleColorMode } = useColorMode();
    
    return (
        <Container maxW={"900px"}>
            <Box px={4} mx={4} borderRadius={5} bg={useColorModeValue("gray.200", "gray.700")}>
                <Flex h="16" alignItems={"center"} justifyContent={"space-between"}>
                    <Flex alignItems={"center"} justifyContent={"center"} gap={3} display={{ base: "none", sm: "flex" }}>
                        <img src="/content-management-system.png" alt="system-logo" width={50} height={50} />
                        <Text fontSize={"40px"}>MStarSupply</Text>
                    </Flex>
                    <Flex gap={3} alignItems={"center"}>
                        <Button onClick={toggleColorMode}>
                            {colorMode === "light" ? <IoMoon /> : <LuSun size={20} />}
                        </Button>

                        <CreateMovimentacaoModal setFollowUp={setFollowUp} />
                    </Flex>
                </Flex>
            </Box>
        </Container>
    )
}

export default Navbar