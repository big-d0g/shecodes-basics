/* VARIABLES */

let raceNumber = Math.floor(Math.random() * 1000); /* Randomised race number up to 1000*/

let earlyRunner = false /* Did runner sign up for the early race? */
let runnerAge = 32 /* Runner's age */

/* FUNCTIONS */

if (earlyRunner && runnerAge > 18) {
  raceNumber += 1000; /* If the runner is over 18, add 1000 to the race number */
}

if (earlyRunner && runnerAge > 18) {
  console.log(`Hey Racer # ${raceNumber}, your start time is 9.30am!`); /*If the runner is over 18 and signed to the early race, start is 9-30am*/
} else if (!earlyRunner && runnerAge > 18) {
  console.log(`Hey Racer # ${raceNumber}, your start time is 11.00am!`); /*If runner is over 18 and did not sign for the early race, start is 11-00am*/
} else if (runnerAge === 18) {
  console.log(`Hey Racer # ${raceNumber}, please see the registration desk!`) /* Racers who are exactly 18, see the reg desk*/
} else {
  console.log(`Hey Racer # ${raceNumber}, your start time is 12.30pm!`); /*All racers under 18, start is 12.30*/
}

