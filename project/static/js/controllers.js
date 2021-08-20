myApp.controller('loginController', ['$scope', '$location', 'AuthService', function ($scope, $location, AuthService) {
      $scope.loginForm = {};

      $scope.login = function () {
            $scope.error = false;
            $scope.disabled = true;

            if ($scope.loginForm.email == undefined)
                  $scope.error = true, $scope.errorMessage = "Please don't leave any field empty!";
            else
                  AuthService.register($scope.loginForm.email, $scope.loginForm.passowrd)
                        .then(() => {
                              $location.path('/main');
                        }, () => {
                              $scope.error = true;
                              $scope.errorMessage = "Invalid username and/or password";
                        });
            $scope.disabled = false;
            $scope.loginForm = {};
      }
}]);

myApp.controller('mainController', ['$scope', function ($scope) {

}])

myApp.controller('AppCtrl', ['$scope', '$interval', function ($scope, $interval) {
      $scope.number = 0;
      $interval(function () {
            $scope.number++;
      }, 1000);

      var colors = ['red', 'blue', 'green', 'yellow', 'orange'];
      $scope.colorClass = function (number) {
            return colors[number % colors.length];
      };
}]);