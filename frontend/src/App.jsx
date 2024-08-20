import { useState } from 'react'
import Navbar from "./components/Navbar"
import FollowUpTable from "./components/FollowUpTable"
import MercadoriasGrid from './components/MercadoriasGrid'
import { Stack, Container, Text } from '@chakra-ui/react'

export const BASE_URL = "http://127.0.0.1:5000/api"

function App() {
  const [followUp, setFollowUp] = useState([])
  const [mercadorias, setMercadorias] = useState([])

  return (
    <Stack minH={"100vh"}>
      <Navbar setFollowUp={setFollowUp}/>

      <Container maxW={"1200px"} my={4}>
        <Text fontSize={{ base: "3x1", md: "50"}} fontWeight={"bold"} letterSpacing={"2px"} textTransform={"uppercase"} textAlign={"center"} mb={8}>
          <Text as={"span"} bgGradient={"linear(to-r, cyan.400, blue.500)"} bgClip={"text"}>
            Movimentações
          </Text>
        </Text>

        <FollowUpTable followUp={followUp} setFollowUp={setFollowUp} />

        <Text fontSize={{ base: "3x1", md: "50"}} fontWeight={"bold"} letterSpacing={"2px"} textTransform={"uppercase"} textAlign={"center"} mb={8} mt={6}>
          <Text as={"span"} bgGradient={"linear(to-r, cyan.400, blue.500)"} bgClip={"text"}>
            Mercadorias
          </Text>
        </Text>

        <MercadoriasGrid mercadorias={mercadorias} setMercadorias={setMercadorias} />
      </Container>
    </Stack>
  )
}

export default App
