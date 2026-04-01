class Mahasiswa: 
    nim = 0 
    nama = "" 
    def perkenalan(self): 
        print(f"Halo nama saya {self.nama}") 
    def hello(self, nama): 
            print(f"Halo {nama}, nama saya {self.nama}") 
mahasiswa = Mahasiswa() 
mahasiswa.nama = "Arya" 
mahasiswa.perkenalan() 
mahasiswa.hello("Budi")