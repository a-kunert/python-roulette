<template>
    <div class="p-10 bg-gray-100">
        
        <div class="bg-green-400 border border-gray-800 rounded-xl p-6 grid grid-cols-3">
            <div></div>
            <div class="grid grid-cols-[min-content_min-content_min-content]">
                <div class="grid col-span-3 grid-cols-subgrid border border-yellow-300">
                    <div class="col-start-2 flex items-center justify-center text-amber-300">0</div>
                </div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center text-red-600">1</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center">2</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center text-red-600">3</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center">4</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center text-red-600">5</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center">6</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center text-red-600">7</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center">8</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center text-red-600">9</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center">10</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center text-red-600">11</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center">12</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center text-red-600">13</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center">14</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center text-red-600">15</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center">16</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center text-red-600">17</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center">18</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center text-red-600">19</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center">20</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center text-red-600">21</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center">22</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center text-red-600">23</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center">24</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center text-red-600">25</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center">26</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center text-red-600">27</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center">28</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center text-red-600">29</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center">30</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center text-red-600">31</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center">32</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center text-red-600">33</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center">34</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center text-red-600">35</div>
              <div class="border border-yellow-300 size-12 flex items-center justify-center">36</div>

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

const getColor = (number) => {
    return {
      "red": "text-red-500",
      "black": "text-black",
      "green": "text-yellow-300"  
    }[number.color]
}


</script>
