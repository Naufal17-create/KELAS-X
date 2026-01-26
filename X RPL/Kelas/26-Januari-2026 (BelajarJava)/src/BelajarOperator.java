/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author MyPC PRO
 */
public class BelajarOperator {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int a = 10;
        int b = 3;
        int penjumlahan = a + b;
        System.out.println("Hasil penjumalahan 2 angka adalah: " + penjumlahan);
        
        int c = 10;
        int d = 3;
        int pengurangan = c - d;
        System.out.println("Hasil pengurangan 2 angka adalah: " + pengurangan);
        
        int r = 10;
        int v = 3;
        int perkalian = r * v;
        System.out.println("Hasil perkalian 2 angka adalah: " + perkalian);
        
        int j = 20;
        int z = 4;
        double pembagian = j / z;
        System.out.println("Hasil pembagian 2 angka adalah: " + pembagian);
        
        int h = 21;
        int i = 4;
        int modulus = h % i;
        System.out.println("Hasil modulus 2 angka adalah: " + modulus);
        
        int k = 20;
        c +=5;
        System.out.println(c);
        
        a-=2;
        System.out.println(a);
        
        b *=100;
        System.out.println(b);
        
        //    operator penugasan
    
        //  = memberi nilai
        a = 3;
        System.out.println(a);
        
        //    += ppenjumlahan nilai
        b+=3;
        System.out.println(b);

        //    =- pengurangan nilai
        c-=3;
        System.out.println(c);

        //    *= perkalian nilai
        b *= 4;
        System.out.println(b);

        //  /= pembagian nilai\
        a/=4;
        System.out.println(a);

        //    %= memoduluskan nilai
        c%=5;
        System.out.println(c);
        
        int p = 50;
        int y = 40;
        
        boolean hasil1 = p == y;
        boolean hasil2 = p >= y;
        boolean hasil3 = p != y;
        boolean hasil4 = p <= y;
        System.out.println(hasil1);
        System.out.println(hasil2);
        System.out.println(hasil3);
        System.out.println(hasil4);
        
       
        
        boolean result = true & true;
        boolean result2 = p>y && p==y;
        boolean result3 = true || true;
        boolean result4 = p!=y || p<y;
        System.out.println("Operator logika - 1 " + result);
        System.out.println("Operator logika - 2 " + result2);
        System.out.println("Operator logika - 3 " + result3);
        System.out.println("Operator logika - 4 " + result4);
           }
}
