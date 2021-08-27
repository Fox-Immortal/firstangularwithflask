myApp.controller("loginController", [
      "$scope",
      "$location",
      "AuthService",
      function ($scope, $location, AuthService) {
            $scope.loginForm = {};

            $scope.login = function () {
                  $scope.error = false;
                  $scope.disabled = true;
                  if ($scope.loginForm == undefined)
                        ($scope.error = true),
                              ($scope.errorMessage = "Please don't leave any field empty!");
                  else if (AuthService.isLoggedIn()) {
                        ($scope.error = true),
                              ($scope.errorMessage =
                                    "User already logged in you need to logout first");
                  } else
                        AuthService.login(
                              $scope.loginForm.email,
                              $scope.loginForm.password
                        ).then(
                              () => {
                                    $location.path("/main");
                              },
                              () => {
                                    $scope.error = true;
                                    $scope.errorMessage = "Invalid username and/or password";
                              }
                        );
                  $scope.disabled = false;
                  $scope.loginForm = {};
            };
            $scope.register = function () {
                  $scope.registerError = false;
                  $scope.disabled = true;

                  if ($scope.registerForm == undefined)
                        ($scope.error = true),
                              ($scope.registerErrorMessage = "Please don't leave any field empty!");
                  else
                        AuthService.register(
                              $scope.registerForm.email,
                              $scope.registerForm.password,
                              $scope.registerForm.email
                        ).then(
                              () => {
                                    $location.path("/main");
                              },
                              () => {
                                    $scope.error = true;
                                    $scope.registerErrorMessage = "Invalid username and/or password";
                              }
                        );
                  $scope.disabled = false;
                  $scope.registerForm = {};
            };
      },
]);


myApp.filter('users', function () {
      return function (students, search) {
            searchStudents = [];
            for (var i = 0; i < students.length; i++) {
                  let keys = Object.keys(students[i]).map(function (key) {
                        return key;
                  });
                  for (let j = 0; j < keys.length; j++)
                        if (keys[j] == 'skills') {
                              let skillKeys = Object.keys(students[i][keys[j]]).map(function (key) {
                                    return key;
                              });
                              for (let k = 0; k < students[i]['skills'].length; k++) {
                                    if (students[i]['skills'][k].name.toLowerCase().includes(search.toLowerCase()))
                                          searchStudents.push(students[i]);
                              }
                        }
                        else if (keys[j] != '$$hashKey' && students[i][keys[j]].toLowerCase().includes(search.toLowerCase()))
                              searchStudents.push(students[i]);
            }
            return searchStudents;
      }
});

myApp.controller("mainController", [
      "$scope",
      function ($scope) {


            localStudents = [
                  { name: 'John', id: '31801002099', skills: [{ name: 'Ios', level: 90 }] },
                  { name: 'Jeff', id: '31801002059', skills: [{ name: 'JEFF', level: 55 }] },
                  { name: 'Mary', id: '31801002098', skills: [{ name: 'AngularJS', level: 67 }] },
                  { name: 'Mike', id: '31601002099', skills: [{ name: 'ReactJs', level: 44 }] },
                  { name: 'Adam', id: '30301013109', skills: [{ name: 'Flask', level: 13 }] },
                  { name: 'Julie', id: '20401213105', skills: [{ name: 'Flutter', level: 15 }] },
                  { name: 'Juliette', id: '20301213105', skills: [{ name: 'Swift', level: 100 }] },
                  { name: 'Juliette', id: '20301213105', skills: [{ name: 'Swift', level: 91 }] },
                  { name: 'Juliette', id: '20301213105', skills: [{ name: 'Swift', level: 95 }] },
                  { name: 'Juliette', id: '20301213105', skills: [{ name: 'Swift', level: 63 }] },
                  { name: 'Juliette', id: '20301213105', skills: [{ name: 'Swift', level: 49 }] },
            ]

            var index = 0;
            $scope.students = [];
            setInterval(() => {
                  if (index < localStudents.length) {
                        $scope.students.push(localStudents[index++]);
                        // $scope.students = localStudents;
                        $scope.$apply();
                  }
            }, 15);
            $scope.searching = false;





            // line chart
            $scope.onClick = function (points, evt) {
                  console.log(points, evt);
            };
            $scope.labels = ["S1", "S2", "SS", "S3", "S4", "S5", "S6"];

            $scope.colors = [
                  "#ff6384",
                  "#EBD725",
                  "#228BEB",
                  "#46BFBD",
                  "#FDB45C",
                  "#949FB1",
                  "#4D5360",
            ];

            style = {
                  borderWidth: 1,
                  borderColor: 'rgpa(0, 0, 0, 0)',
                  pointBorderWidth: 0,
                  pointRadius: 0,
                  pointHitRadius: 0,
            }

            $scope.datasetOverride = [
                  style,
                  style,
                  style,
            ];
            $scope.data = [
                  [25, 40, 60, 50, 35, 40, 100], //red
                  [30, 60, 75, 60, 50, 40, 70], // yellow
                  [50, 30, 22, 30, 50, 80, 60], // blue
            ];

            style = {
                  borderWidth: 1,
                  borderColor: "rgpa(0, 0, 0, 0)",
                  pointBorderWidth: 0,
                  pointRadius: 0,
                  pointHitRadius: 0,
            };

            $scope.datasetOverride = [style, style, style];

            // radar chart
            $scope.radarLabels = ["Typing", "Problem Solving", "Listening", "Business", "Coding", "Design", "Animation"];

            $scope.radarData = [
                  [30, 30, 35, 40, 50, 80, 85],
                  [0, 0, 0, 0, 0, 0, 0],
            ];

            $scope.skillLevel = function (value) {
                  return {
                        "width": value + '%',
                        "height": "74px",
                        "background-color": "#228beb",
                        "opacity": "0.7",
                        "border-radius": "97px",
                  };
            }

      },
]);

myApp.controller("AppCtrl", [
      "$scope",
      "$interval",
      function ($scope, $interval) {
            $scope.number = 0;
            $interval(function () {
                  $scope.number++;
            }, 1000);

            var colors = ["red", "blue", "green", "yellow", "orange"];
            $scope.colorClass = function (number) {
                  return colors[number % colors.length];
            };
      },
]);


myApp.controller("clubsController", [
      "$scope", "$location", function ($scope, $location) {
            $scope.clubs = [];
            for (let i = 0; i < 30; i++)
                  $scope.clubs.push(i);
            $scope.club = function gotoClub() {
                  $location.path('/club');
            }
      }
]);

myApp.controller("clubController", [
      "$scope", function ($scope) {
            $scope.members = [];
            for (var i = 0; i < 30; i++)
                  $scope.members.push(i);
      }
]);