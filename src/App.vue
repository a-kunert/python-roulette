<template>
    <div class="p-10 bg-gray-100">

        <div class="bg-green-500 to-green-700 bg-linear-to-tr border border-gray-800 rounded-xl p-6 grid grid-cols-2">

            <div>
                <div class="mb-4">
                    <div>
                        Balance
                    </div>
                    <div>
                        {{ balance }} €
                    </div>
                </div>

                <div>Stake</div>
                <div>
                    <input class="p-1 w-36 border-green-800 border rounded-md bg-green-300"
                           type="number" min="0" :max="balance" v-model="stake">
                </div>

                <div>
                    {{ bet }}
                </div>


                <div class="mt-12">
                    <button
                        class="transition-colors border border-green-800 rounded-md py-2 px-6 font-semibold hover:bg-green-800 hover:text-green-100"
                        @click="playGame">Play
                    </button>
                </div>

                <div class="mt-12">

                    <div class="size-10 border border-green-800 rounded-md">
                        {{ currentNumber }}
                    </div>
                </div>

            </div>

            <div class="grid grid-cols-2">
                <div class=" flex flex-col mt-10 items-end font-semibold">

                    <div class="grid grid-cols-2 border-y border-l border-yellow-400 h-120">
                        <div class="border-r border-yellow-400">
                            <div
                                class="border-b border-yellow-400 w-15 h-20 flex items-center justify-center text-yellow-300  font-serif text-2xl">
                                <div class="[writing-mode:vertical-lr]">
                                    1-18
                                </div>
                            </div>

                            <div
                                class="border-b border-yellow-400 w-15 h-20 flex items-center justify-center text-yellow-300  font-serif text-2xl"
                                @click="setBet('Parity','Even')">
                                <div class="[writing-mode:vertical-lr]">
                                    Even
                                </div>
                            </div>

                            <div
                                class="border-b border-yellow-400 w-15 h-20 flex items-center justify-center text-yellow-300  font-serif text-2xl">
                                <div class="scale-y-125">
                                    <div class="size-6 bg-black rotate-45 ">
                                    </div>

                                </div>
                            </div>

                            <div
                                class=" border-b border-yellow-400 w-15 h-20 flex items-center justify-center text-yellow-300  font-serif text-2xl">

                                <div class="scale-y-125">
                                    <div class="size-6 bg-[#D00000] rotate-45 ">
                                    </div>

                                </div>
                            </div>

                            <div
                                class=" border-b border-yellow-400 w-15 h-20 flex items-center justify-center text-yellow-300  font-serif text-2xl"
                                @click="setBet('Parity','Odd')">
                                <div class="[writing-mode:vertical-lr]">
                                    Odd
                                </div>
                            </div>

                            <div
                                class=" border-yellow-400 w-15 h-20 flex items-center justify-center text-yellow-300  font-serif text-2xl">
                                <div class="[writing-mode:vertical-lr]">
                                    19-36
                                </div>
                            </div>
                        </div>

                        <div>
                            <DozenBlock :dozen="1"></DozenBlock>
                            <DozenBlock :dozen="2"></DozenBlock>
                            <DozenBlock :dozen="3"></DozenBlock>
                        </div>


                    </div>


                </div>

                <div class="flex  flex-col items-start">
                    <div
                        class="border-x border-t border-yellow-400 w-48 h-10 flex items-center justify-center text-yellow-300  font-serif text-2xl">
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
                            v-for="number in RouletteNumbers.filter(number => number.number !== 0)"
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

    </div>


</template>


<script setup>
import { ref } from 'vue'
import RouletteNumbers from './src/RouletteNumbers.js'
import DozenBlock from './components/DozenBlock.vue'

const balance = ref(1000)

const bet = ref(null)

function setBet(type, value) {
    bet.value = {
        type: type,
        value: value
    }

}

const currentNumber = ref(null)

function playGame() {
    currentNumber.value = Math.round(Math.random() * 36)
    if (!bet.value || bet.value.type !== "Parity") {
        return
    }
    balance.value = balance.value - stake.value
    if (
        bet.value.value === "Even" && currentNumber.value % 2 === 0 ||
        bet.value.value === "Odd" && currentNumber.value % 2 === 1) {
        balance.value = balance.value + 2 * stake.value
    }


}


const stake = ref(0)




function getColor(number) {
    return {
        "red": "text-[#D00000]",
        "black": "text-black",
        "green": "text-yellow-300"
    }[number["color"]]
}


</script>
