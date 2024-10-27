import { ActivityIndicator, FlatList, Pressable, StyleSheet, Text, View } from 'react-native'
import React, { useEffect, useState } from 'react'

//React navigation
import { NativeStackScreenProps } from "@react-navigation/native-stack"
import {RootStackPramList} from "../App"

import ProductItem from '../components/ProductItem'
import Separator from '../components/Seperator'

// data
// import { PRODUCTS_LIST } from '../data/constants'

import { fetchAllItems } from '../api/apiService'

type HomeProps = NativeStackScreenProps<RootStackPramList, "Home">

const Home = ({navigation}: HomeProps) => {
    const [items, setItems] = useState<Product[]>();
    const [loading, setLoading] = useState<boolean>(true);

    useEffect(() => {
        const getItems = async () => {
          try {
            const data = await fetchAllItems();
            setItems(data);
          } catch (error) {
            console.error('Failed to fetch items:', error);
          } finally {
            setLoading(false);
          }
        };
    
        getItems();
      }, []);

      if (loading) {
        return <ActivityIndicator size="large" color="#0000ff" />;
      }

  return (
    <View style={styles.container}>
      <FlatList
      data={items}
      keyExtractor={item => item.id.toString()}
      ItemSeparatorComponent={Separator}
      renderItem={({item}) => (
        <Pressable
        onPress={() => {
          navigation.navigate('Details', {
            product: item
          })
        }}
        >
          <ProductItem product={item}/>
        </Pressable>
      )}
      />
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'flex-start',
    justifyContent: 'center',

    padding: 12,
    backgroundColor: '#FFFFFF',
  },
});

export default Home