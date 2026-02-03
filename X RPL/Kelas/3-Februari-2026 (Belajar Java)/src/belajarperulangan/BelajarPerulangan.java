/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package belajarperulangan;

/**
 *
 * @author MyPC PRO
 */
public class BelajarPerulangan {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        for (int i = 0; i < 12; i++) {
            System.out.println("Darwis");
        }
        
        
//        increment
        for (int z = 1; z <= 5; z++ ) {
            for(int b = 1; b<=z; b++) {
            System.out.print("*");
            }
            System.out.println();
        }
        
        
        System.out.println("");
//        decrement
        
        for (int a = 5; a >= 1; a--) {
            for (int c = 1; c <= a; c++) {
            System.out.print("*");
            }
            System.out.println();
        }
        
        System.out.println("");
//        kanan atas

        for (int q = 5; q >= 1; q--) {
            for (int p = 0; p < 5 - q; p++) {
                System.out.print(" ");
            }
            for (int v = 1; v <= q; v++) {
                System.out.print("*");
            }
            System.out.println();
        }
        
                
    }
    
    
}
