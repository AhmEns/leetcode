class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            birlesik = []
            
            curr = list1
            while curr:
                birlesik.append(curr.val)
                curr = curr.next
                
            curr = list2
            while curr:
                birlesik.append(curr.val)
                curr = curr.next

            n = len(birlesik)
            for i in range(n):
                for j in range(n):
                    if birlesik[i] < birlesik[j]:
                        x = birlesik[i]
                        birlesik[i] = birlesik[j]
                        birlesik[j] = x
            
            dummy = ListNode(0)
            sonuc_curr = dummy
            for deger in birlesik:
                sonuc_curr.next = ListNode(deger)
                sonuc_curr = sonuc_curr.next
            
            return dummy.next