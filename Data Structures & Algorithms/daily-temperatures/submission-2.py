class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        colder_temps = []
        for i in range(len(temperatures)): 
            for j in range(i + 1, len(temperatures)):
                if (temperatures[i] >= temperatures[j]):
                    colder_temps.append(temperatures[j])
                if (temperatures[i] < temperatures[j]):
                    result[i] = len(colder_temps) + 1
                    colder_temps = []
                    break
            colder_temps = []
        return result
        