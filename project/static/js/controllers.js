myApp.controller('loginController', ['$scope', '$location', function ($scope, $location) {

      $scope.login = function () {
            // initial values
            $scope.error = false;
            $scope.disabled = true;

            // handle success
            // alert($scope.loginForm.email);
            $location.path('/main');
            //     $scope.disabled = false;
            //     $scope.loginForm = {};

            // handle error

            // $scope.error = true;
            // $scope.errorMessage = "Invalid username and/or password";
            // $scope.disabled = false;
            // $scope.loginForm = {};
      }
}]);

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