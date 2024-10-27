import { Image, StyleSheet, Text, View } from 'react-native'
import React, { PropsWithChildren } from 'react'


type ProductProps = PropsWithChildren<{
    product: Product
}>

const ProductItem = ({product}: ProductProps) => {
  return (
    <View style={styles.container}>
      <Image 
      source={{uri: product.image}}
      style={styles.image}
      />

      <View>
        <Text style={styles.name}>{product.item_name}</Text>
            <View style={[styles.rowContainer, styles.priceContainer]}>
                <Text style={styles.originalPrice}>
                    ₹{product.original_price.toLocaleString()}
                </Text>
                <Text style={styles.discountPrice}>
                    ₹{product.current_price.toLocaleString()}
                </Text>
                <Text style={styles.offerPercentage}>
                    %{product.discount_percentage} off
                </Text>
        </View>
      </View>

    </View>
  )
}


const styles = StyleSheet.create({
    container: {
      margin: 8,
      flexDirection: 'row',
    },
    rowContainer: {
      flexDirection: 'row',
    },
    image: {
      width: 1080/16,
      height: 1920/16,
      resizeMode: 'contain',
    borderRadius: 8,
      marginRight: 12,
    },
    name: {
      marginBottom: 4,
  
      fontSize: 15,
      fontWeight: '500',
    },
    ratingContainer: {
      marginBottom: 8,
    },
    priceContainer: {
      marginBottom: 12,
    },
    rating: {
      borderRadius: 4,
      paddingHorizontal: 8,
      justifyContent: 'center',
      backgroundColor: '#008c00',
  
      marginRight: 4,
    },
    ratingText: {
      color: '#fff',
      fontSize: 12,
      fontWeight: '600',
    },
    ratingCount: {
      color: '#878787',
    },
    originalPrice: {
      fontSize: 18,
      marginRight: 4,
      fontWeight: '600',
  
      color: 'rgba(0, 0, 0, 0.5)',
      textDecorationLine: 'line-through',
    },
    discountPrice: {
      fontSize: 18,
      marginRight: 4,
      fontWeight: '600',
  
      color: '#000000',
    },
    offerPercentage: {
      fontSize: 17,
      fontWeight: '600',
      color: '#4bb550',
    },
  });

export default ProductItem