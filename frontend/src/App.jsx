import { useState } from 'react'
import Navbar from "./components/Navbar"
import { Stack } from '@chakra-ui/react'

export const BASE_URL = "http://127.0.0.1:5000/api"

function App() {
  const [followUp, setFollowUp] = useState([])

  return (
    <Stack minH={"100vh"}>
      <Navbar setFollowUp={setFollowUp}/>
    </Stack>
  )
}

export default App
