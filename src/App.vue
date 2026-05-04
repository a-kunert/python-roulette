<template>
    <div class="p-10 bg-gray-100">
        
        <div class="bg-green-400 border border-gray-800 rounded-xl p-6 grid grid-cols-3">
            <div></div>
            <div class="grid grid-cols-[min-content_min-content_min-content]">
              <div 
                  class="border border-yellow-300 size-12 flex items-center justify-center" 
                  :class="getColor(number)"
                  v-for="number in numbers">{{number.number}}</div>

            </div>
            <div></div>
            
            
        </div>
        
    </div>
</template>


<script setup>



const numbers = [
    {"number": 0, "color": "green"},
    {"number": 1, "color": "red"},
    {"number": 2, "color": "black"},
    {"number": 3, "color": "red"},
    {"number": 4, "color": "black"},
    {"number": 5, "color": "red"},
    {"number": 6, "color": "black"},
    {"number": 7, "color": "red"},
    {"number": 8, "color": "black"},
    {"number": 9, "color": "red"},
    {"number": 10, "color": "black"},
    {"number": 11, "color": "black"},
    {"number": 12, "color": "red"},
    {"number": 13, "color": "black"},
    {"number": 14, "color": "red"},
    {"number": 15, "color": "black"},
    {"number": 16, "color": "red"},
    {"number": 17, "color": "black"},
    {"number": 18, "color": "red"},
    {"number": 19, "color": "red"},
    {"number": 20, "color": "black"},
    {"number": 21, "color": "red"},
    {"number": 22, "color": "black"},
    {"number": 23, "color": "red"},
    {"number": 24, "color": "black"},
    {"number": 25, "color": "red"},
    {"number": 26, "color": "black"},
    {"number": 27, "color": "red"},
    {"number": 28, "color": "black"},
    {"number": 29, "color": "black"},
    {"number": 30, "color": "red"},
    {"number": 31, "color": "black"},
    {"number": 32, "color": "red"},
    {"number": 33, "color": "black"},
    {"number": 34, "color": "red"},
    {"number": 35, "color": "black"},
    {"number": 36, "color": "red"}
]


function getColor(number) {
    return {
        "red": "text-red-500",
        "black": "text-black",
        "green": "text-yellow-300"
    }[number["color"]]
}


</script>
