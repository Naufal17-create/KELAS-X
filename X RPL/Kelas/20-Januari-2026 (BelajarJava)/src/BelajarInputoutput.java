
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
public class BelajarInputoutput {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner inputUser = new Scanner(System.in);

        System.out.print("masukkan nama anda: ");
        String nama = inputUser.nextLine();
        
        
        System.out.print("Berapakah nomer absen anda: ");
       int absen = inputUser.nextInt();
        
        System.out.print("Berapa uang saku anda: ");
        double uang = inputUser.nextDouble();
        
                
        System.out.print("Abjad apa yang paling kamu suka: ");
        Scanner masukan = new Scanner(System.in);
        String simbol = masukan.nextLine();

                
        System.out.println("nama anda adalah: " + nama);
        System.out.println("nomer absen anda: " + absen);
        System.out.println("Uang saku anda adalah: " + uang);        
        System.out.println("Abjad yang kamu suka: " + simbol);

    }
    
}
