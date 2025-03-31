
-- Clean up sample data if needed
DELETE FROM applied;
DELETE FROM positions;
DELETE FROM companies;
DELETE FROM users;

-- Insert sample user
INSERT INTO users (
    usrid, level, email, first_name, last_name, school, password_hash, created_at, updated_at, autho
) VALUES (
    'yj2860', 'NewGrad', 'yj2860@example.com', 'Youngjin', 'Jung', 'Columbia University', 'fake_hash_here', '2025-03-30 19:24:09', '2025-03-30 19:24:09', 'admin'
);

-- Insert sample companies (industry values corrected)
INSERT INTO companies (cpid, cpname, industry, importance, headquarter, created_at, updated_at, updated_by)
VALUES
  ('CTDL', 'Citadel', 'HedgeFund', 1, '830 Brickell Plaza, Miami, FL 33131, USA', '2025-03-30', '2025-03-30', 'Youngjin'),
  ('CTDSEC', 'Citadel Securities', 'QuantTrading', 1, '830 Brickell Plaza, Miami, FL 33131, USA', '2025-03-30', '2025-03-30', 'Youngjin'),
  ('JANEST', 'Jane Street', 'QuantTrading', 1, '250 Vesey Street, New York, NY 10281, USA', '2025-03-30', '2025-03-30', 'Youngjin'),
  ('MILLEN', 'Millennium Management', 'HedgeFund', 1, '399 Park Avenue, New York, NY 10022, USA', '2025-03-30', '2025-03-30', 'Youngjin'),
  ('GLDMAN', 'Goldman Sachs', 'InvestmentBank', 1, '200 West Street, New York, NY 10282, USA', '2025-03-30', '2025-03-30', 'Youngjin'),
  ('JPMC', 'JPMorgan Chase', 'InvestmentBank', 1, '383 Madison Avenue, New York, NY 10179, USA', '2025-03-30', '2025-03-30', 'Youngjin'),
  ('BLROCK', 'BlackRock', 'AssetManagement', 1, '55 East 52nd Street, New York, NY 10055, USA', '2025-03-30', '2025-03-30', 'Youngjin'),
  ('FIDLTY', 'Fidelity', 'AssetManagement', 1, '245 Summer Street, Boston, MA 02210, USA', '2025-03-30', '2025-03-30', 'Youngjin'),
  ('SNPGLB', 'S&P Global', 'FinancialServices', 1, '55 Water Street, New York, NY 10041, USA', '2025-03-30', '2025-03-30', 'Youngjin'),
  ('CME', 'CME Group', 'Exchange', 1, '20 South Wacker Drive, Chicago, IL 60606, USA', '2025-03-30', '2025-03-30', 'Youngjin'),
  ('MOODYS', 'Moody''s', 'FinancialServices', 1, '7 World Trade Center, 250 Greenwich Street, New York, NY 10007, USA', '2025-03-30', '2025-03-30', 'Youngjin'),
  ('ALLNZ', 'Allianz', 'Insurance', 1, 'Allianz SE, Königinstraße 28, 80802 Munich, Germany', '2025-03-30', '2025-03-30', 'Youngjin');

-- Insert sample positions
INSERT INTO positions (
    pztid, cpid, pztname, pztlevel, year, url, jd, note, recent, active, created_at, updated_at, updated_by, oa_first
) VALUES
('20250330_intern_1', 'CTDL', 'Quantitative Trading - Intern', 'Intern', 2025, 'https://example.com/citadel2025intern1', 'JD', '', FALSE, TRUE, '2025-03-30 19:24:09', '2025-03-30 19:24:09', 'yj2860', FALSE),
('20250330_intern_2', 'CTDL', 'Trading Fundamental Analyst - Summer Intern', 'Intern', 2025, 'https://example.com/citadel2025intern2', 'JD', '', FALSE, TRUE, '2025-03-30 19:24:09', '2025-03-30 19:24:09', 'yj2860', TRUE),
('20250330_newgrad_1', 'CTDL', 'Quantitative Research Analyst - Full Time', 'NewGrad', 2025, 'https://example.com/citadel2025ft1', 'JD', '', FALSE, TRUE, '2025-03-30 19:24:09', '2025-03-30 19:24:09', 'yj2860', TRUE),
('20250330_intern_3', 'JPMC', 'Quantitative Research - Summer Associate', 'Intern', 2025, 'https://example.com/jpm2025qa', 'JD', '', FALSE, TRUE, '2025-03-30 19:24:09', '2025-03-30 19:24:09', 'yj2860', FALSE),
('20250330_intern_4', 'JPMC', 'Quant Trader - Summer Associate', 'Intern', 2025, 'https://example.com/jpm2025qt', 'JD', '', FALSE, TRUE, '2025-03-30 19:24:09', '2025-03-30 19:24:09', 'yj2860', TRUE);

-- Insert sample applied data
INSERT INTO applied (usrid, cpid, pztid, applied, applied_at) VALUES
('yj2860', 'CTDL', '20250330_intern_1', TRUE, '2025-03-30 20:00:00'),
('yj2860', 'CTDL', '20250330_intern_2', TRUE, '2025-03-30 20:00:00'),
('yj2860', 'CTDL', '20250330_newgrad_1', TRUE, '2025-03-30 20:00:00'),
('yj2860', 'JPMC', '20250330_intern_3', TRUE, '2025-03-30 20:00:00'),
('yj2860', 'JPMC', '20250330_intern_4', TRUE, '2025-03-30 20:00:00');
