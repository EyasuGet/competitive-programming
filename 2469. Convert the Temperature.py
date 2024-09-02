class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        
        """
        array=[]
        fahr = celsius + 273.15
        kev = celsius*1.80 + 32.00
        array.append(fahr)
        array.append(kev)
        return array

        