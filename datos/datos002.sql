-- Insertar datos de mentores
INSERT INTO auth_user (username, password, email, first_name, last_name, is_staff, is_active, is_superuser, date_joined)
VALUES
  ('jessyarmoa', 'pbkdf2_sha256$260000$TYd0ktCh1f3s$FubJc6r0UDrCqWsl3fG8GgINxqWJmYLR1/7Ks9ZGvN0=', 'jessyarmoa@gmail.com', 'Jessica', 'Armoa', 0, 1, 0, NOW()),
  ('brxndxz', 'pbkdf2_sha256$260000$TYd0ktCh1f3s$FubJc6r0UDrCqWsl3fG8GgINxqWJmYLR1/7Ks9ZGvN0=', 'brendahuemer@gmail.com', 'Brenda', 'Huemer', 0, 1, 0, NOW());

--Obtener id de los users
SELECT id into @jessy_user_id FROM auth_user WHERE email = 'jessyarmoa@gmail.com';
SELECT id into @brenda_user_id FROM auth_user WHERE email = 'brendahuemer@gmail.com';

-- Insertar datos de mentores en la tabla app_mentor
INSERT INTO app_mentor (user_id, description, website, github, linkedin, created_at, updated_at)
VALUES
  (@jessy_user_id, 'Estudiante de ingenieria en informatica y profesora de programacion inicial con tres años de experiencia', '', 'https://github.com/jessica-armoa', 'https://www.linkedin.com/in/jessica-armoa/', NOW(), NOW()),
  (@brenda_user_id, 'Full stack developer Python con experiencia en desarrollo web con Django y Flask', '', 'https://github.com/jessica-armoa', 'https://www.linkedin.com/in/jessica-armoa/', NOW(), NOW());

-- Obtener ID del mentor Jessy
SELECT id INTO @jessy_mentor_id FROM app_mentor WHERE user_id = @jessy_user_id;

-- Obtener ID del mentor Brenda
SELECT id INTO @brenda_mentor_id FROM app_mentor WHERE user_id = @brenda_user_id;

-- Insertar datos de disponibilidades para Jessy
INSERT INTO app_availability (hour, mentor_id)
VALUES
  ('2023-10-09 20:00:00', @jessy_mentor_id),
  ('2023-10-10 11:00:00', @jessy_mentor_id),
  ('2023-10-10 12:00:00', @jessy_mentor_id),
  ('2023-10-10 13:00:00', @jessy_mentor_id),
  ('2023-10-10 13:30:00', @jessy_mentor_id),
  ('2023-10-11 15:00:00', @jessy_mentor_id),
  ('2023-10-11 20:00:00', @jessy_mentor_id),
  ('2023-10-11 20:30:00', @jessy_mentor_id);

-- Insertar datos de disponibilidades para Brenda
INSERT INTO app_availability (hour, mentor_id)
VALUES
  ('2023-10-09 20:00:00', @brenda_mentor_id),
  ('2023-10-10 11:00:00', @brenda_mentor_id),
  ('2023-10-10 12:00:00', @brenda_mentor_id),
  ('2023-10-10 13:00:00', @brenda_mentor_id),
  ('2023-10-10 13:30:00', @brenda_mentor_id),
  ('2023-10-11 15:00:00', @brenda_mentor_id),
  ('2023-10-11 20:00:00', @brenda_mentor_id),
  ('2023-10-11 20:30:00', @brenda_mentor_id);

COMMIT;
