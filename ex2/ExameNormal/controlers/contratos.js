const Contrato = require('../models/contratos');

module.exports.list = async () => {
  return await Contrato
    .find()
    .exec();
}

module.exports.findById = id => {
  return Contrato
    .findOne({ _id: id })
    .exec();
}

module.exports.insert = contrato => {
  return Contrato.create(contrato);
}

module.exports.removeById = id => {
  return Contrato.deleteOne({ _id: id });
}

module.exports.update = (id, contrato) => {
  return Contrato.updateOne({ id: id }, contrato);
}