class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        my_dict   = {}
        for string in cpdomains:
            cout  = 0
            numbers =  ""
            while string[cout] !=  " ":
                numbers += string[cout]
                cout +=  1
            actual_numbers =  int(numbers)
            domain =  string[cout+1:]
            split_domain =  domain.split(".")
            #print(split_domain)
            for i in range(len(split_domain)):
                sub_domain =  ".".join(split_domain[i:])
                my_dict[sub_domain] = my_dict.get(sub_domain,0) +  actual_numbers
        result  =  []
        for i in my_dict:
            result.append(str(my_dict[i]) + " " + i)
        return result 
                
                
        