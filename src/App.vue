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

                          <RangeBlock
                              range="Low"
                              :bet="bet"
                              @click="setBet('Range', 'Low')"
                          ></RangeBlock>

                          <ParityBlock
                              parity="Even"
                              :bet="bet"
                              @click="setBet('Parity', 'Even')"
                          ></ParityBlock>

                          <ColorBlock
                              color="red" :bet="bet"
                              @click="setBet('color', 'red')"
                          ></ColorBlock>

                          <ColorBlock
                              color="black" :bet="bet"
                              @click="setBet('color', 'black')"
                          ></ColorBlock>

                          <ParityBlock
                              parity="Odd"
                              :bet="bet"
                              @click="setBet('Parity', 'Odd')"
                          ></ParityBlock>

                          <RangeBlock
                              range="High"
                              :bet="bet"
                              @click="setBet('Range', 'High')"
                          ></RangeBlock>

                        </div>

                        <div>
                            <DozenBlock :dozen="1" @click="setBet('Dozen', 1)"></DozenBlock>
                            <DozenBlock :dozen="2" @click="setBet('Dozen', 2)"></DozenBlock>
                            <DozenBlock :dozen="3" @click="setBet('Dozen', 3)"></DozenBlock>
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

                        <ColumnBlock
                            column = "1" :bet="bet"
                            @click="setBet('column', '1')"
                        ></ColumnBlock>

                        <ColumnBlock
                            column = "2" :bet="bet"
                            @click="setBet('column', '2')"
                        ></ColumnBlock>

                        <ColumnBlock
                            column = "3" :bet="bet"
                            @click="setBet('column', '3')"
                        ></ColumnBlock>

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
import ColorBlock from "./components/ColorBlock.vue";
import ColumnBlock from "./components/ColumnBlock.vue";
import ParityBlock from "./components/ParityBlock.vue";
import RangeBlock from "./components/RangeBlock.vue";

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
