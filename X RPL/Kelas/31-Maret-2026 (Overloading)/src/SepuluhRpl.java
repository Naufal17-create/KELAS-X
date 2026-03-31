public class SepuluhRpl {

    
    public static void main(String[] args) {
        MuridRpl objek= new MuridRpl();
        System.out.println(objek.nama);
        System.out.println("Nama Anda adalah: "+ objek.nama);
        objek.nama="JONI";
        System.out.println(objek.nama);
        System.out.println(objek.absen=20);
        System.out.println(objek.hobi);
        System.out.println("");
        System.out.println("");
        
        objek.DataSiswa();
        
        int Tampilanluas=objek.MenghitungPersegi();
        System.out.println("Luas Persegi adalah "+Tampilanluas);
        System.out.println(objek.MenghitungPersegi());
    }
    
}