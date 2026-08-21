class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # 1. Başı kaybetmemek için boş bir sahte düğüm oluştur
        dummy = ListNode(0)
        current = dummy
        carry = 0  # Elde

        # 2. Listelerden biri bitene veya elde kalmayana kadar tek döngüde dön
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            toplam = val1 + val2 + carry
            carry = toplam // 10          # Onlar basamağı (yeni elde)
            digit = toplam % 10           # Birler basamağı

            # Yeni basamağı zincirin ucuna ekle ve ilerle
            current.next = ListNode(digit)
            current = current.next

            # Varsa bir sonraki düğüme geç
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # dummy'nin kendisi sahte olduğundan gerçek liste dummy.next ile başlar
        return dummy.next