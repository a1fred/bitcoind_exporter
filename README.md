# Bitcoind prometheus exporter

![grafana dashboard](dashboard.png)

 * Tested with `bitcoind v0.21`
 * [metrics response example](docs/metrics.sample)
 * [example docker-compose.yml](docker-compose.yml)
 * [grafana dashboard](staff/grafana/dashboards/bitcoind.json)

# Collectors
 * `bestblock` - `bestblock*` metrics, uses `getblock(bestblockhash)` rpc call
 * `estimaterawfee` - `estimaterawfee*` metrics, uses `estimaterawfee` rpc call
 * `estimatesmartfee` - `estimatesmartfee*` metrics, uses `estimatesmartfee` rpc call
 * `getblockchaininfo` - `getblockchaininfo*` metrics, uses `getblockchaininfo` rpc call
 * `getmemoryinfo` - `getmemoryinfo*` metrics, uses `getmemoryinfo` rpc call
 * `getmempoolinfo` - `getmempoolinfo*` metrics, uses `getmempoolinfo` rpc call
 * `getmininginfo` - `getmininginfo*` metrics, uses `getmininginfo` rpc call
 * `getnettotals` - `getnettotals*` metrics, uses `getnettotals` rpc call
 * `getnetworkinfo` - `getnetworkinfo*` metrics, uses `getnetworkinfo` rpc call
 * `uptime` - `uptime` metric, uses `uptime` rpc call

# Environment variables
 * `HOST` listen host, default:`localhost`
 * `PORT` listen port, default:`8064`
 * `BITCOIND` bitcoind url, default:`http://bitcoind:bitcoind@localhost:8335`
 * `COLLECTORS` comma separated list of enabled collectors, all by default

# Docker container
Docker container available at `ghcr.io/a1fred/bitcoind_exporter`.

`amd64` and `arm64` arch supported.

# TODO
 * Action test on bitcoind `0.19`, `0.20`, `0.21`, `22`, `23`
