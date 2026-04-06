public class NaufalMethods {

    // Method 1: Menyapa dengan nama Naufal
    public void sapaNaufal() {
        System.out.println("Halo, saya Naufal!");
    }

    // Method 2: Mengembalikan jumlah huruf dari nama "Naufal"
    public int hitungPanjangNamaNaufal() {
        String nama = "Naufal";
        return nama.length();
    }

    // Method 3: Menerima input umur dan menampilkan perkenalan Naufal
    public String perkenalanNaufal(int umur) {
        return "Nama saya Naufal, umur saya " + umur + " tahun.";
    }

    // Contoh penggunaan (opsional)
    public static void main(String[] args) {
        NaufalMethods nm = new NaufalMethods();

        nm.sapaNaufal();
        int panjang = nm.hitungPanjangNamaNaufal();
        System.out.println("Panjang nama Naufal: " + panjang);
        String perkenalan = nm.perkenalanNaufal(17);
        System.out.println(perkenalan);
    }
}