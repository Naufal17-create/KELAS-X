
import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author MyPC PRO
 */
public class BelajarPercabangan {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner InputUser = new Scanner(System.in);
        System.out.print("Input nilai anda: ");
        int nilai = InputUser.nextInt();
        System.out.println(nilai);
            
        if (nilai <0 || nilai > 100) {
                System.out.println("nilai tidak valid");
      
        } else if (nilai <=20 || nilai <=60 ){ 
            System.out.println("D");
           
    } else if (nilai <= 61 || nilai <=79) {
            System.out.println("C");
    } else if (nilai <=80 || nilai <=89) {
        System.out.println("B");
    }else if (nilai <=100 || nilai <=90) {
            System.out.println("A");
    }    
}
