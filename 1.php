<?php
// Fungsi-fungsi Pencarian
// function cariAbsensi($daftar, $target) {
//     foreach ($daftar as $i => $v) if ($v === $target) return $i;
//     return -1;
// }

// $hasil1 = cariAbsensi(["Budi", "Siti", "Rian", "Andi"], "Rian");
// echo "1. Absensi 'Rian': " . ($hasil1 !== -1 ? "posisi ke-" . ($hasil1 + 1) : "Data tidak ditemukan") . "\n";



// function cariBarang($tumpukan, $target) {
//     foreach ($tumpukan as $i => $v) if ($v === $target) return $i;
//     return -1;
// }

// $hasil2 = cariBarang(["Dompet", "Kunci Motor", "Buku"], "Kunci Motor");
// echo "2. Lost & Found 'Kunci Motor': " . ($hasil2 !== -1 ? "posisi ke-" . ($hasil2 + 1) : "Data tidak ditemukan") . "\n";



// function cariBuku($daftarSeri, $target) {
//     $low = 0; $high = count($daftarSeri) - 1;
//     while ($low <= $high) {
//         $mid = floor(($low + $high) / 2);
//         if ($daftarSeri[$mid] == $target) return $mid;
//         if ($daftarSeri[$mid] < $target) $low = $mid + 1;
//         else $high = $mid - 1;
//     }
//     return -1;
// }

// $hasil3 = cariBuku([101, 102, 105, 110], 105);
// echo "3. Buku Seri 105: " . ($hasil3 !== -1 ? "posisi ke-" . ($hasil3 + 1) : "Data tidak ditemukan") . "\n";



// function cariRanking($skorList, $target) {
//     $low = 0; $high = count($skorList) - 1;
//     while ($low <= $high) {
//         $mid = floor(($low + $high) / 2);
//         if ($skorList[$mid] == $target) return $mid;
//         if ($skorList[$mid] < $target) $high = $mid - 1;
//         else $low = $mid + 1;
//     }
//     return -1;
// }

// $hasil4 = cariRanking([990, 950, 890, 800], 890);
// echo "4. Ranking Skor 890: " . ($hasil4 !== -1 ? "posisi ke-" . ($hasil4 + 1) : "Data tidak ditemukan") . "\n";



// function cariKamus($kamus, $target) {
//     $low = 0; $high = count($kamus) - 1;
//     while ($low <= $high) {
//         $mid = floor(($low + $high) / 2);
//         if ($kamus[$mid] === $target) return $mid;
//         if ($kamus[$mid] < $target) $low = $mid + 1;
//         else $high = $mid - 1;
//     }
//     return -1;
// }

// $hasil5 = cariKamus(["Algorithm", "Binary", "Data"], "Algorithm");
// echo "5. Kamus 'Algorithm': " . ($hasil5 !== -1 ? "posisi ke-" . ($hasil5 + 1) : "Data tidak ditemukan") . "\n";
?>