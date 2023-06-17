#!/usr/bin/node
exports.converter = function (base) {
<<<<<<< HEAD
  return number => number.toString(base);
};
=======
  return function (x) {
    return x.toString(base);
  };
};
>>>>>>> f2c204d42e56c929512c49df13fe2be6a9deb652
