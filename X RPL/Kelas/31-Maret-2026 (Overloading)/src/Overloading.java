public class Overloading {

    void DataKelas(String namakelas){
        System.out.println("Kelas kita adalah" + namakelas);
    }
    void DataKelas(String namakelas,int jmlsiswa){
        System.out.println("Kelas kita adalah" + namakelas);
        System.out.println("Jumlah siswa kelas kita " + jmlsiswa);
    }
}
