class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            # 1. Elemanları toplamak için boş bir liste oluşturuyoruz
            birlesik = []
            
            # 2. list1'deki düğümleri tek tek gezip değerlerini alıyoruz
            curr = list1
            while curr:
                birlesik.append(curr.val)
                curr = curr.next
                
            # 3. list2'deki düğümleri tek tek gezip değerlerini alıyoruz
            curr = list2
            while curr:
                birlesik.append(curr.val)
                curr = curr.next

            # 4. Sizin yazdığınız sıralama mantığı (Bubble Sort)
            n = len(birlesik)
            for i in range(n):
                for j in range(n):
                    if birlesik[i] < birlesik[j]:
                        x = birlesik[i]
                        birlesik[i] = birlesik[j]
                        birlesik[j] = x
            
            # 5. LeetCode bizden 'ListNode' yapısında sonuç beklediği için 
            # sıraladığımız listeyi tekrar bağlı listeye dönüştürüyoruz.
            dummy = ListNode(0)
            sonuc_curr = dummy
            for deger in birlesik:
                sonuc_curr.next = ListNode(deger)
                sonuc_curr = sonuc_curr.next
            
            return dummy.next