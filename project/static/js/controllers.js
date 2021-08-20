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

myApp.controller("mainController", [
      "$scope",
      function ($scope) {
            Chart.defaults.global.tooltips.titleFontSize = 30;
            Chart.defaults.global.tooltips.bodyFontSize = 30;
            Chart.defaults.global.tooltips.footerFontSize = 30;
            $scope.onClick = function (points, evt) {
                  console.log(points, evt);
            };

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
            localStudents = [
                  { name: 'John', id: '31801002099', skill: 'Ios' },
                  { name: 'Mary', id: '31801002098', skill: 'AngularJS' },
                  { name: 'Mike', id: '31601002099', skill: 'ReactJs' },
                  { name: 'Adam', id: '30301013109', skill: 'Flask' },
                  { name: 'Julie', id: '20401213105', skill: 'Flutter' },
                  { name: 'Juliette', id: '20301213105', skill: 'Swift' },
                  { name: 'Juliette', id: '20301213105', skill: 'Swift' },
                  { name: 'Juliette', id: '20301213105', skill: 'Swift' },
                  { name: 'Juliette', id: '20301213105', skill: 'Swift' }];
            var index = 0;
            $scope.students = [];
            setInterval(() => {
                  if (index < localStudents.length)
                        $scope.students.push(localStudents[index++]);
                  // $scope.students = localStudents;
                  $scope.$apply();
            }, 15);
            $scope.searching = false;


            $scope.data = [
                  [25, 40, 60, 50, 35, 40, 80], //red
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
