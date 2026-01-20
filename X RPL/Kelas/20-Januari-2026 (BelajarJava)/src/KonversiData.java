/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author MyPC PRO
 */
public class KonversiData {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        System.out.println("Belajar konversi data");
        System.out.println("");
        
        String a = "25";
//        int b = Integer.valueOf(a);

        int c = Integer.parseInt(a);
        System.out.println(c + 100);
        
        String d = String.valueOf(c);
        System.out.println(d + 100);
        
    }
    
}
