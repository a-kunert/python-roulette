<template>
    <div class="p-10 bg-gray-100">

        <div class="bg-[#049B04] border border-gray-800 rounded-xl p-6 grid grid-cols-2">

            <div class=" flex flex-col mt-10 items-end">

              <div class="grid grid-cols-2 border-y border-l border-yellow-400 h-120">
                <div class="border-r border-yellow-400">
                  <div>
                    <div
                        class="border-b border-yellow-400 w-15 h-20 flex items-center justify-center text-yellow-300 font-extrabold font-serif text-2xl">
                      <div class="[writing-mode:vertical-lr]">
                        1-18
                      </div>

                    </div>
                  </div>

                  <div>
                    <div
                        class="border-b border-yellow-400 w-15 h-20 flex items-center justify-center text-yellow-300 font-extrabold font-serif text-2xl">
                      <div class="[writing-mode:vertical-lr]">
                        Even
                      </div>
                    </div>
                  </div>

                  <div>
                    <div
                        class="border-b border-yellow-400 w-15 h-20 flex items-center justify-center text-yellow-300 font-extrabold font-serif text-2xl">
                      <div class="[writing-mode:vertical-lr]">
                        Black
                      </div>
                    </div>
                  </div>

                  <div>
                    <div
                      class=" border-b border-yellow-400 w-15 h-20 flex items-center justify-center text-yellow-300 font-extrabold font-serif text-2xl">
                      <div class="[writing-mode:vertical-lr]">
                        Red
                      </div>
                    </div>

                  <div>
                    <div
                      class=" border-b border-yellow-400 w-15 h-20 flex items-center justify-center text-yellow-300 font-extrabold font-serif text-2xl">
                      <div class="[writing-mode:vertical-lr]">
                        Odd
                      </div>
                    </div>
                  </div>

                  <div>
                    <div
                      class=" border-yellow-400 w-15 h-20 flex items-center justify-center text-yellow-300 font-extrabold font-serif text-2xl">
                      <div class="[writing-mode:vertical-lr]">
                        19-36
                      </div>
                    </div>
                  </div>




                  </div>

                </div>

                <div>
                  <div
                      class=" border-b border-yellow-400 w-15 h-40 flex items-center justify-center text-yellow-300 font-extrabold font-serif text-2xl">
                    <div class="[writing-mode:vertical-lr]">
                      1st 12
                    </div>

                  </div>

                  <div
                      class="border-b border-yellow-400 w-15 h-40 flex items-center justify-center text-yellow-300 font-extrabold font-serif text-2xl">
                    <div class="[writing-mode:vertical-lr]">
                      2nd 12
                    </div>

                  </div>

                  <div
                      class=" border-yellow-400 w-15 h-40 flex items-center justify-center text-yellow-300 font-extrabold font-serif text-2xl">
                    <div class="[writing-mode:vertical-lr]">
                      3rd 12
                    </div>

                  </div>
                </div>


              </div>



              </div>

            <div class="flex  flex-col items-start">
                <div
                    class="border-x border-t border-yellow-400 w-48 h-10 flex items-center justify-center text-yellow-300 font-extrabold font-serif text-2xl">
                    0
                </div>

                <div class="grid grid-cols-3">

                    <div
                        class="border-l border-t border-yellow-400 w-16 h-10 flex items-center justify-center font-serif text-2xl font-extrabold"
                        :class="[
                            getColor(number), 
                        number.number % 3 === 0 ? 'border-r' : '',
                        number.number > 33 ? 'border-b' : '',
                  ]"
                        v-for="number in numbers.filter(number => number.number !== 0)"
                        :key="number.number"
                    >
                        {{ number.number }}
                    </div>

                </div>

                <div class="grid grid-cols-3">
                    <div class="border-b border-l border-yellow-400 w-16 h-10"></div>
                    <div class="border-b border-l border-yellow-400 w-16 h-10"></div>
                    <div class="border-b border-x border-yellow-400 w-16 h-10"></div>
                </div>

            </div>

        </div>

    </div>


</template>


<script setup>


const numbers = [
    { "number": 0, "color": "green" },
    { "number": 1, "color": "red" },
    { "number": 2, "color": "black" },
    { "number": 3, "color": "red" },
    { "number": 4, "color": "black" },
    { "number": 5, "color": "red" },
    { "number": 6, "color": "black" },
    { "number": 7, "color": "red" },
    { "number": 8, "color": "black" },
    { "number": 9, "color": "red" },
    { "number": 10, "color": "black" },
    { "number": 11, "color": "black" },
    { "number": 12, "color": "red" },
    { "number": 13, "color": "black" },
    { "number": 14, "color": "red" },
    { "number": 15, "color": "black" },
    { "number": 16, "color": "red" },
    { "number": 17, "color": "black" },
    { "number": 18, "color": "red" },
    { "number": 19, "color": "red" },
    { "number": 20, "color": "black" },
    { "number": 21, "color": "red" },
    { "number": 22, "color": "black" },
    { "number": 23, "color": "red" },
    { "number": 24, "color": "black" },
    { "number": 25, "color": "red" },
    { "number": 26, "color": "black" },
    { "number": 27, "color": "red" },
    { "number": 28, "color": "black" },
    { "number": 29, "color": "black" },
    { "number": 30, "color": "red" },
    { "number": 31, "color": "black" },
    { "number": 32, "color": "red" },
    { "number": 33, "color": "black" },
    { "number": 34, "color": "red" },
    { "number": 35, "color": "black" },
    { "number": 36, "color": "red" }
]


function getColor(number) {
    return {
        "red": "text-[#D00000]",
        "black": "text-black",
        "green": "text-yellow-300"
    }[number["color"]]
}


</script>
