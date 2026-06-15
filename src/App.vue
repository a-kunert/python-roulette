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

                <div class="mt-13">

                    <div class="size-10 border border-green-800 rounded-md flex items-center justify-center">
                        {{ currentNumber }}
                    </div>
                </div>

                <div class="mt-1">

                    <div class="size-10 border border-green-800 rounded-md flex items-center justify-center">
                      <div class="size-6 rotate-45"
                           :class="{
                            'bg-black': currentColor === 'black',
                            'bg-[#D00000]': currentColor === 'red',
                            'bg-green-800': currentColor === 'green'
                           }">
                      </div>
                    </div>
                </div>


            </div>

            <div class="grid grid-cols-2">
                <div class=" flex flex-col mt-10 items-end font-semibold">

                    <div class="grid grid-cols-2 border-y border-l border-yellow-400 h-120">
                        <div class="border-r border-yellow-400">
                            <div
                                class="border-b border-yellow-400 w-15 h-20 flex items-center justify-center text-yellow-300  font-serif text-2xl"
                                :class="[
                                    isActive('Range', 'Low') ? 'bg-green-800' : ''
                                ]">
                                <div class="[writing-mode:vertical-lr]"
                                @click="setBet('Range', 'Low')">
                                    1-18
                                </div>
                            </div>

                            <div
                                class="border-b border-yellow-400 w-15 h-20 flex items-center justify-center text-yellow-300  font-serif text-2xl"
                                @click="setBet('Parity','Even')"
                                :class="[
                                    isActive('Parity', 'Even') ? 'bg-green-800' : ''
                                ]">
                                <div class="[writing-mode:vertical-lr]">
                                    Even
                                </div>
                            </div>

                            <div
                                class="border-b border-yellow-400 w-15 h-20 flex items-center justify-center text-yellow-300  font-serif text-2xl">
                                <div class="scale-y-125">
                                    <div
                                        class="size-6 bg-black rotate-45 "
                                        @click="setBet('Color', 'Black')"
                                        :class="[
                                          isActive('Color', 'Black') ? 'ring-2 ring-green-800' : ''
                                        ]"

                                    >
                                    </div>

                                </div>
                            </div>

                            <div
                                class=" border-b border-yellow-400 w-15 h-20 flex items-center justify-center text-yellow-300  font-serif text-2xl">

                                <div class="scale-y-125">
                                    <div class="size-6 bg-[#D00000] rotate-45 "
                                    @click="setBet('Color', 'Red')"
                                    :class="[
                                        isActive('Color', 'Red') ? 'ring-2 ring-green-800' : ''
                                    ]"
                                    >
                                    </div>

                                </div>
                            </div>

                            <div
                                class=" border-b border-yellow-400 w-15 h-20 flex items-center justify-center text-yellow-300  font-serif text-2xl"
                                @click="setBet('Parity','Odd')"
                                :class="[
                                    isActive('Parity', 'Odd') ? 'bg-green-800' : ''
                                ]">

                                <div class="[writing-mode:vertical-lr]">
                                    Odd
                                </div>
                            </div>

                            <div
                                class="border-b border-yellow-400 w-15 h-20 flex items-center justify-center text-yellow-300  font-serif text-2xl"
                                :class="[
                                    isActive('Range', 'High') ? 'bg-green-800' : ''
                                ]">
                                <div class="[writing-mode:vertical-lr]"
                                @click="setBet('Range', 'High')">
                                    19-36
                                </div>
                            </div>
                        </div>

                        <div>
                            <DozenBlock :dozen="1" :setBet="setBet"></DozenBlock>
                            <DozenBlock :dozen="2" :setBet="setBet"></DozenBlock>
                            <DozenBlock :dozen="3" :setBet="setBet"></DozenBlock>
                        </div>


                    </div>


                </div>

                <div class="flex  flex-col items-start">
                    <div
                        class="border-x border-t border-yellow-400 w-48 h-10 flex items-center justify-center text-yellow-300  font-serif text-2xl"
                        @click="setBet('Number', 0)">
                        0
                    </div>

                    <div class="grid grid-cols-3">

                        <NumberBlock
                            v-for="number in RouletteNumbers.filter(number => number.number !== 0)"
                            :key="number.number"
                            :number="number"
                            :bet="bet"
                            @click="setBet('Number', number.number)"
                        ></NumberBlock>

                    </div>

                    <div class="grid grid-cols-3">
                        <div class="border-y border-l border-yellow-400 w-16 h-10"
                             @click="setBet('Column', '1')"></div>
                        <div class="border-y border-l border-yellow-400 w-16 h-10"
                             @click="setBet('Column', '2')"></div>
                        <div class="border-y border-x border-yellow-400 w-16 h-10"
                             @click="setBet('Column', '3')"></div>
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
import NumberBlock from './components/NumberBlock.vue'

const balance = ref(1000)

const bet = ref(null)

function setBet(type, value) {
    bet.value = {
        type: type,
        value: value
    }

}

const currentNumber = ref(null)
const currentColor = ref(null)


//Hervorhebung Feld
function isActive(type, value) {
  if (bet.value === null) {
    return false
  }

  if (bet.value.type === type && bet.value.value === value) {
    return true
  }
  return false

}


function playGame() {

  if (!bet.value || stake.value <= 0 || stake.value > balance.value) return
  if (balance.value === 0) return
  if (stake.value > balance.value) return

  currentNumber.value = Math.floor(Math.random() * 37)
  balance.value -= stake.value

  const currentField = RouletteNumbers.find(
      number => number.number === currentNumber.value
  )

  currentColor.value = currentField?.color

  let payout = 0

// Parity
  if (
      bet.value.type === "Parity" &&
      (
          (bet.value.value === "Even" && currentNumber.value !== 0 && currentNumber.value % 2 === 0) ||
          (bet.value.value === "Odd" && currentNumber.value !== 0 && currentNumber.value % 2 === 1)
      )
  ) {
    payout = 2
  }

// Color
  if (
      bet.value.type === "Color" &&
      currentField?.color === bet.value.value.toLowerCase()
  ) {
    payout = 2
  }

// Dozen
  if (bet.value.type === "Dozen") {
    const n = currentNumber.value

    const isWin =
        (bet.value.value === 1 && n >= 1 && n <= 12) ||
        (bet.value.value === 2 && n >= 13 && n <= 24) ||
        (bet.value.value === 3 && n >= 25 && n <= 36)

    if (isWin) payout = 3
  }

// Range
  if (bet.value.type === "Range") {
    const n = currentNumber.value

    const isWin =
        (bet.value.value === "Low" && n >= 1 && n <= 18) ||
        (bet.value.value === "High" && n >= 19 && n <= 36)

    if (isWin) payout = 2
  }

// Number
  if (bet.value.type === "Number") {
    const isWin = bet.value.value === currentNumber.value

    if (isWin) payout = 36
  }

 //Column
  if (bet.value.type === "Column") {
    const n = currentNumber.value

    const isWin =
        (bet.value.value === "1" && n % 3 === 1) ||
        (bet.value.value === "2" && n % 3 === 2) ||
        (bet.value.value === "3" && n % 3 === 0)

    if (isWin) payout = 3
  }

 //Green
  if (bet.value.type === "Green") {
    const isWin = bet.value.value === currentNumber.value

    if (isWin) payout = 36
  }


  if (payout > 0) {
    balance.value += payout * stake.value
  }
}



const stake = ref(0)







</script>
