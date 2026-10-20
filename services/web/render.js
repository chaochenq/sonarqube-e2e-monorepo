function render(req) {
  return eval(req.query.template);
}

module.exports = { render };
