import { Grid, Flex, Spinner, Text } from '@chakra-ui/react'
import React, { useEffect, useState } from 'react'
import MercadoriaCard from './MercadoriaCard'
import { BASE_URL } from '../App';

const MercadoriasGrid = ({mercadorias, setMercadorias}) => {
    const [isLoading, setIsLoading] = useState(true);
    
    useEffect(() => {
        const getMercadorias = async () => {
          try {
            const res = await fetch(BASE_URL + "/mercadorias");
            const data = await res.json();
    
            if(!res.ok) {
              throw new Error(data.error);
            }
            setMercadorias(data);
    
          } catch (error) {
            console.error(error);
          } finally {
            setIsLoading(false);
          }
        }
        getMercadorias();
      },[setMercadorias])

      console.log(mercadorias);
      return (
        <>
            <Grid templateColumns={{
                base: "1fr",
                md: "repeat(2, 1fr)",
                lg: "repeat(3, 1fr)",
            }}
            gap={4}>
                {mercadorias.map((mercadoria) => (
                    <MercadoriaCard key={mercadoria.id} mercadoria={mercadoria} setMercadorias={setMercadorias} />
                ))}
            </Grid>
        </>
      )
}

export default MercadoriasGrid