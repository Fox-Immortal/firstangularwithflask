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