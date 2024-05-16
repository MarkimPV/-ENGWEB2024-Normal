var express = require('express');
var router = express.Router();
var Contrato = require('../controlers/contratos');
const contrato = require('../models/contratos');

/* GET home page. */
router.get('/', async function(req, res, next) {
  listaContratos = await Contrato.list()
  res.render('main', {listaContratos: listaContratos });
});

module.exports = router;
