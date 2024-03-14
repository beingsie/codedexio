// Build two objects for two boarding passes
let departTripTicket =  {
  name: "Sergio",
  from: "California",
  to: "Switzerland",
  businessClass: false,
  upgrade: function () {
    if (departTripTicket.businessClass === true){
      return "Your ticket is already business class!";
    } else {
      departTripTicket.businessClass = true;
      return "You've been upgraded to business class!";
    }
  },
}

let returnTripTicket =  {
  name: "Sergio",
  from: "Switzerland",
  to: "California",
  businessClass: true,
}

// Use the .upgrade() method on at least one of them,
// then log both objects to the console
console.log(departTripTicket);
console.log(departTripTicket.upgrade());

console.log(returnTripTicket);

// Add a .leaveTime and .arriveTime property to both objects (integers 1-24)
departTripTicket.leaveTime = 6;
departTripTicket.arriveTime = 12;

returnTripTicket.leaveTime = 9;
returnTripTicket.arriveTime = 18;

// Bonus ✨

// Define a .flightTime() method property that calculates
// and prints the travel time with the .leaveTime and .arriveTime
departTripTicket.flightTime = function () {
  const travelTime = departTripTicket.arriveTime - departTripTicket.leaveTime;
  return travelTime;
};

returnTripTicket.flightTime = function () {
  const travelTime = returnTripTicket.arriveTime - returnTripTicket.leaveTime;
  return travelTime;
};

console.log(departTripTicket.flightTime());
console.log(returnTripTicket.flightTime());
